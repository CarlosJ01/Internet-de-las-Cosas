"""
    Práctica 8: Almacenamiento local
    Equipo 7
        Castro Cazares Carlos Jahir (Responsable)
        Vieyra Ernesto
    ###################################################################
    Python v3.8
    ------------------------------------------------------------------
    Instalacion de librerias
        NTPLIB => pip install ntplib
        Request => pip install requests
        mySQL => python -m pip install mysql-connector-python

"""
import datetime
import random
import ntplib
import hashlib
import requests
import json
import mysql.connector
import time
from time import ctime

# Genera cadena para la firma
def generar_cadena():
    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
    cadena = ""
    for i in range(1,10):
        cadena += random.choice(caracteres)
    return cadena

# Peticion a la API de Temperatura
def getTemperatura():
    headers = {
        'x-rapidapi-key': "36e38d330amshdf10f3cb12f62dfp163d00jsn039be0388006",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
    parametros = {
        "q": 'Morelia,MX',
        "units": "metric"
    }
    response = requests.request("GET", "https://community-open-weather-map.p.rapidapi.com/weather", headers=headers, params=parametros)
    return response

if __name__ == '__main__':
    while True:
        # Obtener y almacenar fecha/hora
        print('Obtencion del tiempo actual . . .')
        horaEnvio = datetime.datetime.now()
        try:
            request = ntplib.NTPClient().request('time-e-g.nist.gov')
            fechaServidor = datetime.datetime.strptime(ctime(request.tx_time), "%a %b %d %H:%M:%S %Y")
        except:
            fechaServidor = datetime.datetime.now()
            print('Error al conectar con la API')
        horaLlegada = datetime.datetime.now()
        horaReal = str(fechaServidor + ((horaLlegada - horaEnvio) / 2))
        fecha = str(horaReal)[:10]
        hora = str(horaReal)[11:]
        print('Hora y Fecha actual : '+fecha+' '+hora)
        print('##############################################################################################')

        # Obtener y almacenar posición (geolocalización)
        print('Calculando longitud y latitud . . .')
        latitud = "{:.6f}".format(random.uniform(19.723332, 19.723596))
        longitud = "{:.6f}".format(random.uniform(-101.185271, -101.184851))
        utc = -6
        print('Latitud: '+latitud+', Longitud: '+longitud+', UTC: '+str(utc))
        print('##############################################################################################')

        # Asignar ID y crear Firma Digital
        print('Calculando firma digital . . .')
        id = 'Sen-Temp-V-01'
        cadena = generar_cadena()
        firma = (hashlib.md5(cadena.encode())).hexdigest()
        print('Firma Digital con MD5: ' + firma + ', Id del Sensor: '+id)
        print('##############################################################################################')

        # Obtener y almacenar datos del sensor (temperatura)
        print('Obtencion de la temperatura local . . .')
        variable = 'temperatura'
        valor = 0
        try:
            response = getTemperatura()
            if response.status_code == 200:
                valor = json.loads(response.text)["main"]["temp"]
                print('Temperatura actual  de Morelia: ' + str(valor) + '°C, tipo: ' + variable)
            else:
                print('Error en la conexion de la API')
        except:
            print('Error al conectar con la API')
        print('##############################################################################################')

        # Insertar en la Base de Datos
        print('Insertar en la Base de Datos los valores . . .')
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="datos",
            port="3307"
        )
        cursor = mydb.cursor()
        query = "INSERT INTO clima (id, firma, latitud, longitud, utc, fecha, hora, variable, valor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, firma, latitud, longitud, utc, fecha, hora, variable, valor))
        mydb.commit()
        print('_____________________________________________________________________________________________')
        print('Esperando 1 minuto para el siguiente escaneo \n\n')
        time.sleep(60)