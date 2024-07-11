"""
    Práctica 9: Almacenamiento remoto (Programa_1 Cliente)
    Objetivo: Conocer la forma de almacenar información de un dispositivo de IoT en un servidor.
    --------------------------------------------------------------------------------------------
    Equipo 7
        Castro Cazares Carlos Jahir (Responsable)
        Vieyra Ernesto
    ###########################################################################################
    Python v3.8
    Instalacion de librerias
         mySQL => python -m pip install mysql-connector-python
         requests => pip install requests
"""
import mysql.connector
import hashlib
import requests

# Variables Globales
puertoBD = "3307"
urlServidor = 'http://192.168.0.100/IOT/P08/recibir_datos.php'

# Obtener el primer registro no enviado de la Base de Datos
def getUltimoRegistro():
    print('Obteniendo el ultimo registro de la Base Datos . . .')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datos",
        port=puertoBD
    )
    cursor = mydb.cursor()
    query = "SELECT * FROM clima WHERE enviado = 0 LIMIT 1"
    cursor.execute(query)
    datos = cursor.fetchone()
    cursor.close()
    return datos

#Actualizar el registro a enviado
def updateEnvioRegistro(id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datos",
        port=puertoBD
    )
    cursor = mydb.cursor()
    query = "UPDATE clima SET enviado = 1 WHERE id = "+str(id)
    cursor.execute(query)
    cursor.close()

if __name__ == '__main__':
    # Optener el ultimo registro y generar el certificado
    registro = getUltimoRegistro()
    if registro != None:
        certificado = (hashlib.md5((registro[2] + registro[7]).encode())).hexdigest()

        # Generar los datos
        datos = {
            'id_sensor': registro[1],
            'certificado': certificado,
            'latitud': registro[3],
            'longitud': registro[4],
            'utc': registro[5],
            'fecha': registro[6],
            'hora': registro[7],
            'variable': registro[8],
            'valor': registro[9]
        }
        print(datos)

        # Enviar la peticion al Servidor
        print('\nEnviando datos al servidor')
        respuesta = requests.post(urlServidor, data=datos)

        print('Respuesta del servidor: '+respuesta.text)

        if respuesta.text == 'Guardado en la nube satisfactorio':
            print('\nActulizando la base de datos')
            updateEnvioRegistro(registro[0])
    else:
        print('No hay registros por enviar')