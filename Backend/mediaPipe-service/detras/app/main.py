from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from .gesture_detector import detectar_letra_a
import numpy as np
import cv2
import os
from gtts import gTTS
import pytesseract
import subprocess
import time

app = FastAPI()

@app.post("/detectar_gesto")
async def detectar_gesto(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    resultado = detectar_letra_a(img)
    return JSONResponse(content=resultado)

@app.post("/leer_texto")
async def leer_texto(imagen: UploadFile = File(...)):
    nombre_archivo = f"temp_{imagen.filename}"
    with open(nombre_archivo, "wb") as buffer:
        buffer.write(await imagen.read())

    # Procesar imagen
    img = cv2.imread(nombre_archivo)
    texto = pytesseract.image_to_string(img)
    os.remove(nombre_archivo)

    # Guardar como voz
    tts = gTTS(text=texto, lang='en')  # Usa 'es' si quieres español
    archivo_mp3 = "lectura.mp3"
    tts.save(archivo_mp3)
    # Reproducir con VLC
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
    vlc_process = subprocess.Popen([vlc_path, archivo_mp3, '--play-and-exit'])

    # Esperar a que VLC termine de reproducir (tiempo estimado o esperar al proceso)
    time.sleep(10)  # O ajusta según la duración de tu mp3
    
    # Esperar a que VLC termine de reproducir
    vlc_process.wait()
    # Eliminar el archivo .mp3
    if os.path.exists(archivo_mp3):
        os.remove(archivo_mp3)

    return JSONResponse(content={"mensaje": "Texto leído correctamente"})

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Comunicados Sin Barreras"}
