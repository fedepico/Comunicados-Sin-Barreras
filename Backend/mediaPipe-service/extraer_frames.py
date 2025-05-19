import os
import cv2
import glob
from tqdm import tqdm

VIDEOS_DIR = r"E:\Sena-Voz\lsa64_preprocessed\lsa64_hand_videos"
FRAMES_DIR = r"E:\Sena-Voz\dataset_frames"
FRAME_SIZE = (64, 64)
FRAMES_POR_VIDEO = 20
LETRAS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

os.makedirs(FRAMES_DIR, exist_ok=True)

rutas_videos = glob.glob(os.path.join(VIDEOS_DIR, "*.avi"))

print(f"Procesando videos: {len(rutas_videos)} encontrados...")

for ruta_video in tqdm(rutas_videos):
    try:
        nombre_archivo = os.path.basename(ruta_video)
        partes = nombre_archivo.split('_')
        
        letra_idx = int(partes[1]) - 1  # índice de la letra
        letra = LETRAS[letra_idx]

        video_id = os.path.splitext(nombre_archivo)[0]
        output_dir = os.path.join(FRAMES_DIR, letra, video_id)

        # 🔄 Si ya existe la carpeta con los frames, saltar
        if os.path.exists(output_dir):
            print(f"✔️ Ya procesado: {video_id}, se omite.")
            continue

        os.makedirs(output_dir, exist_ok=True)

        cap = cv2.VideoCapture(ruta_video)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        interval = max(1, total_frames // FRAMES_POR_VIDEO)
        count = 0
        saved = 0

        while cap.isOpened() and saved < FRAMES_POR_VIDEO:
            ret, frame = cap.read()
            if not ret:
                break
            if count % interval == 0:
                frame = cv2.resize(frame, FRAME_SIZE)
                frame_path = os.path.join(output_dir, f"{saved:03d}.jpg")
                cv2.imwrite(frame_path, frame)
                saved += 1
            count += 1

        cap.release()

    except Exception as e:
        print(f"⚠️ Error procesando {ruta_video}: {e}")
        continue

print("✅ Extracción de frames finalizada.")