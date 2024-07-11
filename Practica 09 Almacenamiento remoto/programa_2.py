"""
    Práctica 9: Almacenamiento remoto (Programa_2 Servidor)
    Objetivo: Conocer la forma de almacenar información de un dispositivo de IoT en un servidor.
    --------------------------------------------------------------------------------------------
    Equipo 7
        Castro Cazares Carlos Jahir (Responsable)
        Vieyra Ernesto
    ###########################################################################################
    Python v3.8
    Instalacion de librerias
         mySQL => python -m pip install mysql-connector-python
"""
import mysql.connector
import hashlib

# Variables Globales
puertoBD = "3307"

def getUltimoRegistro():
    print('Obteniendo el ultimo registro de la Base Datos . . .')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datos_servidor",
        port=puertoBD
    )
    cursor = mydb.cursor()
    query = "SELECT * FROM clima WHERE revisado = 0"
    cursor.execute(query)
    datos = cursor.fetchall()
    cursor.close()
    return datos

def getFirma(idSensor):
    print('\nObteniendo la firma del sensor . . .')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datos_servidor",
        port=puertoBD
    )
    cursor = mydb.cursor()
    query = "SELECT firma FROM firma_sensores WHERE id_sensor = '"+idSensor+"' LIMIT 1"
    cursor.execute(query)
    datos = cursor.fetchone()
    cursor.close()
    return datos[0]

def marcarRevisado(id):
    print('Marcar como revisado . . .')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datos_servidor",
        port=puertoBD
    )
    cursor = mydb.cursor()
    query = "UPDATE clima SET revisado = 1 WHERE id = " + str(id)
    cursor.execute(query)
    cursor.close()

def eliminarRegisro(id):
    print('Eliminando . . .')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datos_servidor",
        port=puertoBD
    )
    cursor = mydb.cursor()
    query = "DELETE FROM clima WHERE id = " + str(id)
    cursor.execute(query)
    cursor.close()

if __name__ == '__main__':
    # Optener todos los datos no revisados
    registros = getUltimoRegistro()

    if len(registros) == 0:
        print('No hay registros por revisar')
    else:
        print('Revisando registros en la Base de Datos')
        for registro in registros:
            # Obteniendo firma y generando certificado 2
            firma = getFirma(registro[1])
            certificado1 = registro[2]
            certificado2 = (hashlib.md5((firma + registro[7]).encode())).hexdigest()

            #Comparando Certificado
            if certificado1 == certificado2:
                # Si es igual se marca como revisado
                print("Registro Confiable: " + str(registro))
                marcarRevisado(registro[0])
            else:
                # Si es diferente Borra el registro
                print("* Registro no confiable: " + str(registro))
                eliminarRegisro(registro[0])


