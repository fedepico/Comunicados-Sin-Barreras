# Microservicio Backend – Comunicados Sin Barreras

Este microservicio forma parte del aplicativo "Comunicados Sin Barreras", diseñado para ayudar a personas sordomudas a traducir lenguaje de señas a texto mediante visión computacional con MediaPipe.

## 🚀 Funcionalidad
- Recibe una imagen (JPEG) desde un cliente o frontend.
- Detecta si el gesto representa la letra "A" en lenguaje de señas.
- Retorna una respuesta JSON con el gesto detectado y el nivel de confianza.

---

## 📦 Requisitos
- Python 3.9 o superior
- Pip

## 🧱 Instalación
1. Clona el repositorio y entra al proyecto:
```bash
git clone https://github.com/tu-usuario/repositorio.git
cd repositorio
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución del servidor
Desde la raíz del repositorio, ejecuta:
```bash
uvicorn backend.app.main:app --reload
```

Abre en tu navegador:
```
http://127.0.0.1:8000/docs
```
Ahí encontrarás la documentación interactiva del API.

---

## 📤 Pruebas
Puedes enviar una imagen de prueba con el archivo `test_api_request.py`:

```bash
python test_api_request.py
```

Modifica el archivo para apuntar a una imagen válida:
```python
ruta_imagen = "mano_letra_a.jpg"
```

---

## 🛠 Estructura del backend
```
backend/
├── app/
│   ├── main.py               # API con FastAPI
│   ├── gesture_detector.py   # Lógica de reconocimiento
│   └── __init__.py
├── test_api_request.py       # Script de prueba del API
├── requirements.txt          # Dependencias
```

---

## 🤝 Colaboradores
Este módulo forma parte del trabajo colaborativo en microservicios del equipo del proyecto "Comunicados Sin Barreras".

---

## 📬 Contacto
Federico Gomez  
Desarrollador backend – rama-python  