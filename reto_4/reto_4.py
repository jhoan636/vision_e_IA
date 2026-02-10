import cv2
import numpy as np


# ROJO: en HSV el rojo "envuelve" el hue, por eso tiene 2 rangos
RED1_LOWER = np.array([0, 120, 70])
RED1_UPPER = np.array([10, 255, 255])
RED2_LOWER = np.array([170, 120, 70])
RED2_UPPER = np.array([180, 255, 255])

GREEN_LOWER = np.array([35, 80, 60])
GREEN_UPPER = np.array([85, 255, 255])

BLUE_LOWER = np.array([90, 80, 60])
BLUE_UPPER = np.array([130, 255, 255])

colors_hsv = [
    ("Rojo",  (RED1_LOWER, RED1_UPPER, RED2_LOWER, RED2_UPPER)),
    ("Verde", (GREEN_LOWER, GREEN_UPPER)),
    ("Azul",  (BLUE_LOWER, BLUE_UPPER)),
]

kernel = np.ones((5, 5), np.uint8)


# CAPTURA DE VIDEO
cap = cv2.VideoCapture(0)  # 0 = webcam principal

if not cap.isOpened():
    raise RuntimeError("No se pudo abrir la cámara. Prueba con 1 o revisa permisos.")

min_area = 800  # evita detectar ruido pequeño

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    best_label = None
    best_area = 0
    best_box = None

    # Probar cada color y quedarnos con el más grande
    for item in colors_hsv:
        label = item[0]

        if label == "Rojo":
            r1_low, r1_up, r2_low, r2_up = item[1]
            mask1 = cv2.inRange(hsv, r1_low, r1_up)
            mask2 = cv2.inRange(hsv, r2_low, r2_up)
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            low, up = item[1]
            mask = cv2.inRange(hsv, low, up)

        # Limpiar ruido (morfología)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)

        # Contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            continue

        c = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(c)

        if area > best_area and area > min_area:
            x, y, w, h = cv2.boundingRect(c)
            best_area = area
            best_label = label
            best_box = (x, y, w, h)

    # Dibujar resultado final
    if best_box is not None:
        x, y, w, h = best_box

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        text = f"{best_label}"
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Seguimiento y clasificacion (3 colores)", frame)

    # ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
