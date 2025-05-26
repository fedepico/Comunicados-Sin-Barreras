from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from PIL import Image
import shutil
import os
import cv2
import requests

from modelo_inferencia import predict_sign  # Asegúrate de que este archivo exista

app = FastAPI()

# Configuración de rutas estáticas y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 📌 Función OCR usando API externa OCR.Space
def leer_texto_desde_imagen(img_path):
    url = 'https://api.ocr.space/parse/image'
    with open(img_path, 'rb') as f:
        files = {'file': (img_path, f)}
        payload = {
            'apikey': 'K86595358688957',  # Cambia por la tuya real si la revocan
            'language': 'spa'
        }
        response = requests.post(url, data=payload, files=files)
        resultado = response.json()
        if resultado.get("ParsedResults"):
            return resultado["ParsedResults"][0]["ParsedText"].strip()
        return "[No se detectó texto]"

# 🏠 Página principal
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 📷 Lectura de texto desde imagen (modo invidente)
@app.post("/leer_texto", response_class=HTMLResponse)
async def leer_texto(request: Request, imagen: UploadFile = File(...)):
    ruta = "temp.png"
    with open(ruta, "wb") as f:
        shutil.copyfileobj(imagen.file, f)
    texto = leer_texto_desde_imagen(ruta)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "texto": texto,
        "origen": "imagen"
    })

# ✋ Detección de señas desde video (modo sordomudo)
@app.post("/senas", response_class=HTMLResponse)
async def detectar_sena(request: Request, video: UploadFile = File(...)):
    ruta = "temp_video.mp4"
    with open(ruta, "wb") as f:
        shutil.copyfileobj(video.file, f)

    cap = cv2.VideoCapture(ruta)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval = max(total_frames // 20, 1)
    frames = []

    for i in range(20):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * interval)
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
    cap.release()

    letra = predict_sign(frames) if len(frames) == 20 else "⛔ Video muy corto"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "texto": letra,
        "origen": "video"
    })

# 📍 Ubicación simulada para activar funciones automáticamente
lugares_registrados = [
    {"nombre": "Biblioteca Pública", "lat": 4.6097, "lon": -74.0818, "accion": "leer_texto"},
    {"nombre": "Hospital Central", "lat": 4.6100, "lon": -74.0825, "accion": "senas"}
]

@app.get("/ubicacion", response_class=JSONResponse)
async def detectar_ubicacion(lat: float, lon: float):
    for lugar in lugares_registrados:
        if abs(lugar["lat"] - lat) < 0.001 and abs(lugar["lon"] - lon) < 0.001:
            return {"lugar": lugar["nombre"], "accion": lugar["accion"]}
    return {"lugar": "No registrado", "accion": "ninguna"}

# ✋ Simulación de sensor de proximidad
@app.get("/sensor/proximidad", response_class=JSONResponse)
async def sensor_proximidad():
    return {"activado": True}

# 📶 Lectura NFC simulada
@app.get("/nfc", response_class=JSONResponse)
async def leer_nfc(contenido: str):
    if contenido == "punto123":
        return {"info": "Estás frente a la estación central. Puedes activar el lector de texto."}
    return {"info": "Etiqueta desconocida o no registrada."}
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from PIL import Image
import shutil
import os
import cv2
import requests

from modelo_inferencia import predict_sign  # Asegúrate de que este archivo exista

app = FastAPI()

# Configuración de rutas estáticas y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 📌 Función OCR usando API externa OCR.Space
def leer_texto_desde_imagen(img_path):
    url = 'https://api.ocr.space/parse/image'
    with open(img_path, 'rb') as f:
        files = {'file': (img_path, f)}
        payload = {
            'apikey': 'K86595358688957',  # Cambia por la tuya real si la revocan
            'language': 'spa'
        }
        response = requests.post(url, data=payload, files=files)
        resultado = response.json()
        if resultado.get("ParsedResults"):
            return resultado["ParsedResults"][0]["ParsedText"].strip()
        return "[No se detectó texto]"

# 🏠 Página principal
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 📷 Lectura de texto desde imagen (modo invidente)
@app.post("/leer_texto", response_class=HTMLResponse)
async def leer_texto(request: Request, imagen: UploadFile = File(...)):
    ruta = "temp.png"
    with open(ruta, "wb") as f:
        shutil.copyfileobj(imagen.file, f)
    texto = leer_texto_desde_imagen(ruta)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "texto": texto,
        "origen": "imagen"
    })

# ✋ Detección de señas desde video (modo sordomudo)
@app.post("/senas", response_class=HTMLResponse)
async def detectar_sena(request: Request, video: UploadFile = File(...)):
    ruta = "temp_video.mp4"
    with open(ruta, "wb") as f:
        shutil.copyfileobj(video.file, f)

    cap = cv2.VideoCapture(ruta)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval = max(total_frames // 20, 1)
    frames = []

    for i in range(20):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * interval)
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
    cap.release()

    letra = predict_sign(frames) if len(frames) == 20 else "⛔ Video muy corto"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "texto": letra,
        "origen": "video"
    })

# 📍 Ubicación simulada para activar funciones automáticamente
lugares_registrados = [
    {"nombre": "Biblioteca Pública", "lat": 4.6097, "lon": -74.0818, "accion": "leer_texto"},
    {"nombre": "Hospital Central", "lat": 4.6100, "lon": -74.0825, "accion": "senas"}
]

@app.get("/ubicacion", response_class=JSONResponse)
async def detectar_ubicacion(lat: float, lon: float):
    for lugar in lugares_registrados:
        if abs(lugar["lat"] - lat) < 0.001 and abs(lugar["lon"] - lon) < 0.001:
            return {"lugar": lugar["nombre"], "accion": lugar["accion"]}
    return {"lugar": "No registrado", "accion": "ninguna"}

# ✋ Simulación de sensor de proximidad
@app.get("/sensor/proximidad", response_class=JSONResponse)
async def sensor_proximidad():
    return {"activado": True}

# 📶 Lectura NFC simulada
@app.get("/nfc", response_class=JSONResponse)
async def leer_nfc(contenido: str):
    if contenido == "punto123":
        return {"info": "Estás frente a la estación central. Puedes activar el lector de texto."}
    return {"info": "Etiqueta desconocida o no registrada."}
