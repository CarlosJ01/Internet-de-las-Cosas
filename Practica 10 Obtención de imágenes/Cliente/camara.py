"""
    Práctica 10: Obtención de imágenes
        Objetivo
            Obtener imágenes de una cámara
        Equipo 7
            Castro Cazares Carlos Jahir (Responsable)
            Vieyra Ernesto
    ###########################################################
    Python 3.8.8
    OpenCV => pip install opencv-python
    Requests => pip install requests
"""
import cv2
import uuid
import time
import requests

urlServidor = "http://192.168.100.15/IOT/P10S/php/recibirImagen.php"
urlCliente = "http://192.168.100.15/IOT/P10C/"

if __name__ == '__main__':
    # Ciclo para tomar fotos
    while True:
        # Concexion con la camara
        camara = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        leido, frame = camara.read()
        camara.release()

        # Si extrajo la imagen almacenarla localmente
        nombreImg = ""
        if leido:
            nombreImg = "img/"+str(uuid.uuid4())+".png"
            cv2.imwrite(nombreImg, frame)
            print("Foto tomada correctamente")
        else:
            print("Error al acceder a la cámara")

        # Enviar la imagen al servidor
        if nombreImg != "":
            print('Enviando al servidor: ' + urlServidor)
            respuesta = requests.post(urlServidor, data={'urlImagen': urlCliente+nombreImg})
            print(respuesta.text)
        print('\n')
        
        # Siguente toma en 1 segundo
        time.sleep(1)