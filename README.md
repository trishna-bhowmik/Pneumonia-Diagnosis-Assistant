🩺 Pneumonia Diagnosis Assistant

A Deep Learning powered web application for detecting Pneumonia from chest X-rays.
This project combines a FastAPI backend (PyTorch + Grad-CAM) with a React frontend for easy and intuitive diagnosis visualization.

🚀 Features

📂 Upload chest X-ray images

🤖 Automated prediction using a trained CNN model (pneumonia_cnn.pth)

📊 Confidence score with progress bar

🔥 Grad-CAM heatmap visualization for interpretability

🌐 Modern and responsive React UI


⚙️ Backend Setup (FastAPI + PyTorch)
1. Navigate to backend folder
cd backend

2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run FastAPI server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload


Backend will be available at:
👉 http://localhost:8000
Static Grad-CAM heatmaps served at:
👉 http://localhost:8000/static/...

💻 Frontend Setup (React + Vite + Tailwind)
1. Navigate to frontend folder
cd frontend

2. Install dependencies
npm install

3. Run development server
npm run dev


Frontend will be available at:
👉 http://localhost:5173

📡 API Endpoint

POST /predict/

Input: Image file (.jpg, .png, .jpeg)

Output JSON:

{
  "prediction": "NORMAL" or "PNEUMONIA",
  "class_index": 0 or 1,
  "confidence": 0.987,
  "heatmap_url": "/static/heatmap_xxx.png"
}

🧠 Model

CNN trained on Chest X-ray Dataset (Kaggle – Pneumonia Detection)

Binary classification: NORMAL (0) vs PNEUMONIA (1)

Heatmap generated using Grad-CAM for model interpretability

📸 Demo Screenshots

📂 Upload Chest X-ray → 🧠 Prediction + Confidence → 🔥 Grad-CAM Heatmap

(Add screenshots of your app here)

🔮 Future Improvements

🧾 Add upload history panel (compare multiple predictions)

🌍 Deploy on cloud (Render / AWS / GCP)

👩‍⚕️ Multi-class disease detection (e.g., TB, Covid-19, etc.)

🛡️ Disclaimer

⚠️ This tool is for educational purposes only.
It is not a substitute for professional medical diagnosis.
Always consult a certified radiologist or doctor.

👩‍💻 Author

Developed by Trishna Bhowmik ✨
