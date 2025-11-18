# Script para la detección de ojos abiertos y cerrados con el modelo YOLOv8 y con un video guardado

# import cv2

# from ultralytics import YOLO

# # Dimensiones deseadas (por ejemplo, Full HD)
# screen_width = 1920
# screen_height = 1080

# model = YOLO('trainning/open_close_detect/yolov8n_exp/weights/best.pt')
# cap = cv2.VideoCapture('videoplayback.mp4')
# print("Open status:", cap.isOpened())
# print("FPS:", cap.get(cv2.CAP_PROP_FPS))
# count = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("No se pudo leer el frame o se terminó el video")
#         break
#     count += 1
#     results = model(frame)
#     annotated_frame = results[0].plot()
#     # Redimensionar frame
#     annotated_frame = cv2.resize(annotated_frame, (screen_width, screen_height), interpolation=cv2.INTER_LINEAR)
#     cv2.imshow('Detección ojos abiertos/cerrados', annotated_frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# print(f"Frames leídos: {count}")
# cap.release()
# cv2.destroyAllWindows()


# Script para la detección de ojos abiertos y cerrados con el modelo YOLOv8 y con un la camara de la computadora para tomar capturas

# import cv2
# from ultralytics import YOLO

# # Puedes cambiar el índice si la cámara principal no es la 0
# camara = cv2.VideoCapture(0)  # Usa 1 si tienes más de una cámara y la 0 no funciona

# if not camara.isOpened():
#     print("No se pudo acceder a la cámara")
#     exit()

# model = YOLO('trainning/open_close_detect/yolov8n_exp/weights/best.pt')

# contador = 0
# while True:
#     ret, frame = camara.read()
#     if not ret:
#         print("No se pudo leer el frame de la cámara")
#         break

#     # Detección con YOLO
#     results = model(frame)
#     annotated_frame = results[0].plot()  # Añade las anotaciones al frame

#     # Mostrar la imagen
#     cv2.imshow("Presiona ESPACIO para capturar, Q para salir", annotated_frame)

#     tecla = cv2.waitKey(1) & 0xFF
#     if tecla == ord(' '):  # Barra espaciadora
#         nombre_imagen = f"captura_{contador}.jpg"
#         cv2.imwrite(nombre_imagen, annotated_frame)
#         print(f"Imagen guardada como {nombre_imagen}")
#         contador += 1
#     elif tecla == ord('q'):  # Salir con 'q'
#         break

# camara.release()
# cv2.destroyAllWindows()


# Script para la detección de ojos abiertos y cerrados con el modelo YOLOv8 y con la camara de la computadora para grabar un video

# import cv2
# import numpy as np
# import threading
# import sounddevice as sd
# import soundfile as sf
# from ultralytics import YOLO
# import ffmpeg
# import time

# # Configuración de grabación
# video_filename = 'video.mp4'
# fps = 20  # Cuadros por segundo de la cámara

# # Detector YOLO
# model = YOLO('trainning/open_close_detect/yolov8n_exp/weights/best.pt')

# # Cámara
# camara = cv2.VideoCapture(0)
# if not camara.isOpened():
#     print("No se pudo acceder a la cámara")
#     exit()

# width = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # VideoWriter para guardar el video procesado
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

# # Configuración de audio
# samplerate = 44100
# channels = 1
# audio_data = []

# print("Presiona 'q' para finalizar la grabación.")
# while True:
#     ret, frame = camara.read()
#     if not ret:
#         print("No se pudo leer el frame de la cámara")
#         break

#     results = model(frame)
#     annotated_frame = results[0].plot()
#     out.write(annotated_frame)
#     cv2.imshow("Grabando. Presiona Q para salir", annotated_frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# print("Espere mientras se guarda el archivo...")

# camara.release()
# out.release()
# cv2.destroyAllWindows()
