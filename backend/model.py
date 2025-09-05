import os
import torch
import torch.nn as nn
from torchvision import models, transforms

MODEL_FILENAME = "pneumonia_cnn.pth"
MODEL_PATH = os.path.join(os.path.dirname(__file__), "saved_models", MODEL_FILENAME)


TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

CLASS_NAMES = ["NORMAL", "PNEUMONIA"] 

def load_model(device=None):
    """
    Loads the ResNet model and weights. Returns (model, transform, device).
    Raises FileNotFoundError if MODEL_PATH does not exist.
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Train or copy the .pth into saved_models/")

    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

   
    model = models.resnet18(pretrained=False)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, len(CLASS_NAMES))

    
    state = torch.load(MODEL_PATH, map_location=device)
    model.load_state_dict(state)
    model.to(device)
    model.eval()

    return model, TRANSFORM, device
