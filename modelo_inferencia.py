import numpy as np
import cv2
from tensorflow.keras.models import load_model

FRAMES_POR_VIDEO = 20
FRAME_SIZE = (64, 64)
CLASES = list("ABCDEFGHIJ")

# Cargar modelo SOLO una vez
model = load_model("app/modelos/sign_language_model_reducido.h5")

def predict_sign(frames):
    if len(frames) != FRAMES_POR_VIDEO:
        raise ValueError("Se requieren 20 frames")
    frames_resized = [cv2.resize(f, FRAME_SIZE) for f in frames]
    frames_np = np.array(frames_resized, dtype=np.float32) / 255.0
    entrada = np.expand_dims(frames_np, axis=0)
    pred = model.predict(entrada)
    idx = np.argmax(pred)
    return CLASES[idx]
