# videos-Alfabeto
import os
import requests
from tqdm import tqdm

BASE_URL = "https://raw.githubusercontent.com/facundoq/lsa64/master/Alfabeto/"
LETTERS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
DOWNLOAD_DIR = "lsa64/Alfabeto"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

for letter in tqdm(LETTERS, desc="Descargando videos"):
    for i in range(1, 101):  # Hay 100 videos por letra
        filename = f"{letter}_{i:03}.mpg"
        url = f"{BASE_URL}{filename}"
        path = os.path.join(DOWNLOAD_DIR, filename)

        if not os.path.exists(path):
            response = requests.get(url)
            if response.status_code == 200:
                with open(path, "wb") as f:
                    f.write(response.content)
            else:
                print(f"❌ No se pudo descargar: {url}")
