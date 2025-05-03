import requests

# Ruta al archivo de imagen que contiene un gesto
ruta_imagen = "mano_letra_a.jpg"  # Asegúrate de que exista en el mismo directorio

# Endpoint del microservicio
url = "http://localhost:8000/detectar_gesto"

# Cargar la imagen como archivo
with open(ruta_imagen, "rb") as img:
    files = {"file": (ruta_imagen, img, "image/jpeg")}
    response = requests.post(url, files=files)

# Imprimir la respuesta del backend
print("Respuesta del servidor:", response.json())