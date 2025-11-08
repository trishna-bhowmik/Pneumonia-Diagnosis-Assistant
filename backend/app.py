import os
import io
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware  
from PIL import Image
import torch

from model import load_model, TRANSFORM, CLASS_NAMES
from gradcam_utils import preprocess_pil, run_gradcam_and_save, STATIC_DIR

app = FastAPI(title="Medical Image Diagnosis API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://pneumonia-diagnosis-assistant-3.onrender.com",  # your frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


try:
    model, transform, device = load_model()
except FileNotFoundError as e:
    
    model = None
    transform = TRANSFORM
    device = torch.device("cpu")
    missing_model_error = str(e)
else:
    missing_model_error = None


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Accepts an image file (x-ray) and returns:
    {
      "prediction": "NORMAL" or "PNEUMONIA",
      "class_index": 0 or 1,
      "confidence": 0.987,
      "heatmap_url": "/static/heatmap_...png"
    }
    """
    if missing_model_error:
        raise HTTPException(status_code=500, detail=missing_model_error)

   
    contents = await file.read()
    try:
        pil = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image file: {e}")

  
    input_tensor, np_img = preprocess_pil(pil, transform)
    input_tensor = input_tensor.unsqueeze(0).to(device)

    
    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.softmax(outputs, dim=1).cpu().numpy()[0]
        class_index = int(probs.argmax())
        confidence = float(probs[class_index])
        label = CLASS_NAMES[class_index]

   
    heatmap_url = run_gradcam_and_save(
        model=model,
        device=device,
        input_tensor=input_tensor,
        np_img=np_img,
        target_index=class_index
    )

    return JSONResponse({
        "prediction": label,
        "class_index": class_index,
        "confidence": confidence,
        "heatmap_url": heatmap_url
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
