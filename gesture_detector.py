from Lsa64_Model import predict_sign
import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def detectar_letra_a(imagen):
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.7
    ) as hands:
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        resultados = hands.process(imagen_rgb)

        if not resultados.multi_hand_landmarks:
            return {"gesto": "No detectado", "confianza": 0.0}

        hand_landmarks = resultados.multi_hand_landmarks[0].landmark

        # Validar si los dedos están cerrados (puño cerrado)
        dedo_ids = [8, 12, 16, 20]  # Índice, medio, anular, meñique
        es_puno = all(hand_landmarks[i].y > hand_landmarks[i - 2].y for i in dedo_ids)

        if es_puno:
            return {"gesto": "Letra A", "confianza": 0.95}

        return {"gesto": "Otro", "confianza": 0.5}

def detectar_sena_desde_video(ruta_video):
    cap = cv2.VideoCapture(ruta_video)
    frames = []

    while len(frames) < 20:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    if len(frames) == 20:
        letra = predict_sign(frames)
    else:
        letra = "⛔ Video demasiado corto"

    return letra