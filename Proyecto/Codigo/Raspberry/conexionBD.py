# Conexion con la base de datos
import mysql.connector
import datetime

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="facemask",
        port=3307
    )

def insertarCliente(temperatura, fechaHora):
    # Insertar
    cursor = mydb.cursor()
    query = "INSERT INTO clientes(temperatura, entrada) VALUES(%s, %s)"
    cursor.execute(query, (temperatura, fechaHora))
    mydb.commit()

    #Optener id
    query = "SELECT id FROM clientes WHERE local = 1 LIMIT 1"
    cursor.execute(query)
    datos = cursor.fetchone()
    cursor.close()

    return datos[0]
    
def updateSalida(fechaHora):
    # Obtener id
    cursor = mydb.cursor()
    query = "SELECT id FROM clientes WHERE local = 1 ORDER BY DESC entrada LIMIT 1"
    cursor.execute(query)
    id = cursor.fetchone()[0]

    # Actualizar
    query = f"UPDATE clientes SET salida = {fechaHora}, local = 0 WHERE id = {id}"
    cursor.execute(query)
    cursor.close()
    
    return id
