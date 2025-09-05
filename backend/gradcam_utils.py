import os
import uuid
import numpy as np
from PIL import Image
import cv2
import torch

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from pytorch_grad_cam.utils.image import show_cam_on_image


STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(STATIC_DIR, exist_ok=True)

def preprocess_pil(pil_img, transform):
    """Apply torchvision transform to PIL image and return (tensor, normalized_numpy_rgb)"""
    img_rgb = pil_img.convert("RGB")
   
    np_img = np.array(img_rgb).astype(np.float32) / 255.0
  
    tensor = transform(img_rgb)
    return tensor, np_img

def run_gradcam_and_save(model, device, input_tensor, np_img, target_index=None):
    try:
        target_layer = model.layer4[-1].conv2
    except Exception:
        target_layer = model.layer4[-1]

    if target_index is None:
        with torch.no_grad():
            outputs = model(input_tensor)
            target_index = int(outputs.argmax(dim=1).item())

    cam = GradCAM(model=model, target_layers=[target_layer])

    grayscale_cam = cam(input_tensor=input_tensor, targets=[ClassifierOutputTarget(target_index)])
    cam_map = grayscale_cam[0, :]

   
    np_img_resized = cv2.resize(np_img, (cam_map.shape[1], cam_map.shape[0]))

    
    visualization = show_cam_on_image(np_img_resized, cam_map, use_rgb=True)

   
    fname = f"heatmap_{uuid.uuid4().hex}.png"
    save_path = os.path.join(STATIC_DIR, fname)
    Image.fromarray(visualization).save(save_path)

    return f"/static/{fname}"
