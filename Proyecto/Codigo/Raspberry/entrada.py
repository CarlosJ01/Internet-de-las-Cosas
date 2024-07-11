# Codigo para monitoriar la entrada
import hashlib
import requests
import time
from time import sleep

# Conexion con la Base de Datos
from conexionBD import *

# Sensor MLX90614 
import board
import busio as io
import adafruit_mlx90614

# Sensor de proximidad
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

# IA deteccion cubrebocas
import cv2
import os
import mediapipe as mp

#Url del servidor
urlServidor = 'http://192.168.0.100/facemask/almacenamiento_remoto.php'
firmaDigital = 'HNos6pfF2M*$'

#Abrir camara
mp_face_detection = mp.solutions.face_detection
LABELS = ["Con_mascarilla", "Sin_mascarilla"]

# leer el modelo
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("face_mask_model.xml")
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    
    # Configuracion de pines para el sensor de proximidad
    gpio.init()
    gpio.setcfg(port.PA1, gpio.INPUT)

    while True:
        # Monitoreo de cubrebocas
        ret, frame = cap.read()
        if ret == False: break
        frame = cv2.flip(frame, 1)

        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)

        if results.detections is not None:
            for detection in results.detections:
                xmin = int(detection.location_data.relative_bounding_box.xmin * width)
                ymin = int(detection.location_data.relative_bounding_box.ymin * height)
                w = int(detection.location_data.relative_bounding_box.width * width)
                h = int(detection.location_data.relative_bounding_box.height * height)
                if xmin < 0 and ymin < 0:
                    continue
                #cv2.rectangle(frame, (xmin,ymin), (xmin + w, ymin + h), (0,255,0), 5)

                face_image = frame[ymin : ymin + h, xmin : xmin + w]
                face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                face_image = cv2.resize(face_image, (72,72), interpolation=cv2.INTER_CUBIC)

                result = face_mask.predict(face_image)

                 # Si tiene cubrebocas
                if result[1] < 150:
                    color = (0,255,0) if LABELS[result[0]] == "Con_mascarilla" else (0,0,255)
                    cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (xmin,ymin), (xmin + w, ymin + h), color,2)

                    # Detectar Temperatura, COnfiguras el pin para leer el de temperatura
                    sensorTemperatura = adafruit_mlx90614.MLX90614(io.I2C(board.SCL, board.SDA, frequency=100000))
                    temperatura = "{:.2f}".format(mlx.object_temperature)
                    cv2.putText(frame, f"Temperatura: {temperatura}°C", (0,0), 2, 1, color, 1, cv2.LINE_AA)
                    if temperatura >= 36.1 and temperatura <= 37.2:
                        # Detectar gel
                        if gpio.input(port.PA1) == 1:
                            cv2.putText(frame, f"Puedes pasar", (0,50), 2, 1, color, 1, cv2.LINE_AA)
                            # Insertar un cliente en la base de datos (Almacenamiento Local)
                            fechaHora = datetime.datetime.now()
                            id = insertarCliente(temperatura, fechaHora)
                            # Generar Certificado y data
                            certificado = (hashlib.md5(firmaDigital.encode())).hexdigest()
                            dataSend = {
                                'certificado': certificado,
                                'query': f"INSERT INTO clientes(id, temperatura, entrada) VALUES({id}, {temperatura}, {fechaHora})"
                            }
                            # Enviar al servidor
                            requests.post(urlServidor, data=dataSend)
                            
                            # Dormir para el siguiente cliente 10s
                            time.sleep(10)
                        else:
                            cv2.putText(frame, f"Colocate Gel", (0,50), 2, 1, color, 1, cv2.LINE_AA)
                    else:
                        cv2.putText(frame, f"No tienes una temperatura ideal", (0,50), 2, 1, color, 1, cv2.LINE_AA)
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == 27: 
            break
