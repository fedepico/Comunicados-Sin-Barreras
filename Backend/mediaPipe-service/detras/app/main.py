from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from .gesture_detector import detectar_letra_a

app = FastAPI()

@app.post("/detectar_gesto")
async def detectar_gesto(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    resultado = detectar_letra_a(img)
    return JSONResponse(content=resultado)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Comunicados Sin Barreras"}
