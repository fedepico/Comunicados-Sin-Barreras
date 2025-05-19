from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
import pytesseract
from gtts import gTTS
import cv2
import os

app = FastAPI()

@app.post("/leer_texto")
async def leer_texto(imagen: UploadFile = File(...)):
    # Guardar imagen temporalmente
    nombre_archivo = f"temp_{imagen.filename}"
    with open(nombre_archivo, "wb") as buffer:
        buffer.write(await imagen.read())

    # Verificar si se cargó la imagen correctamente
    img = cv2.imread(nombre_archivo)
    if img is None:
        os.remove(nombre_archivo)
        return JSONResponse(content={"error": "No se pudo leer la imagen"}, status_code=400)

    # Preprocesamiento: convertir a escala de grises y binarizar
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Extraer texto
    texto = pytesseract.image_to_string(thresh, lang="eng+spa")  # usa inglés y español

    # Borrar imagen temporal
    os.remove(nombre_archivo)

    # Verificar si se detectó texto
    if not texto.strip():
        return JSONResponse(content={"texto": "No se detectó texto legible en la imagen."}, status_code=200)

    # Generar archivo de audio con gTTS
    try:
        tts = gTTS(text=texto, lang='es')  # idioma español
        audio_file = "texto_leido.mp3"
        tts.save(audio_file)
    except Exception as e:
        return JSONResponse(content={"error": f"No se pudo generar el audio: {str(e)}"}, status_code=500)

    return FileResponse(audio_file, media_type="audio/mpeg", filename=audio_file)

@app.get("/")
def raiz():
    return {"mensaje": "Servicio OCR para personas invidentes activo."}