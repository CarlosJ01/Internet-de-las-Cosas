# Codigo para controlar la saida
import hashlib
import requests
import time

# Conexion con la Base de Datos
from conexionBD import *

# Sensor de proximidad
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

#Url del servidor
urlServidor = 'http://192.168.0.100/facemask/almacenamiento_remoto.php'
firmaDigital = 'HNos6pfF2M*$'

if __name__ == '__main__':
    # Configuracion del sensor de seres vivos
    gpio.init()
    gpio.setcfg(port.PA3, gpio.INPUT)

    while True:
        # Si detecta movimiento
        if gpio.input(port.PA3) == 1:
            # Actualizar la base de datos con una salida
            fechaHora = datetime.datetime.now()
            id = updateSalida()
            # Generar Certificado y data
            certificado = (hashlib.md5(firmaDigital.encode())).hexdigest()
            dataSend = {
                'certificado': certificado,
                'query':  f"UPDATE clientes SET salida = {fechaHora}, local = 0 WHERE id = {id}"
            }
            # Enviar al servidor
            requests.post(urlServidor, data=dataSend)