# Libreria para conexion con mySQL
# python -m pip install mysql-connector-python

# Librerias
import random
from datetime import date
from datetime import datetime
import time
import mysql.connector

# Conexion con sql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="localizacion",
  port="3307"
)
mycursor = mydb.cursor()

print("############################ Cordenadas creadas ############################")
# Ciclo que crea las cordenadas
while True:
  # Calcular la longitud y latitud
  latitud = "{:.6f}".format(random.uniform(19.723332, 19.723596))
  longitud = "{:.6f}".format(random.uniform(-101.185271, -101.184851))
  fecha = datetime.now()
  print("Latitud: "+str(latitud)+"\tLongitud: "+str(longitud)+"\t Fecha y Hora: "+str(fecha))
  
  # Insertar en la base de datos
  sql = "INSERT INTO movimientos ( Latitud, Longitud, FechaYHora) VALUES (%s, %s,%s)"
  val = (latitud, longitud,fecha)
  mycursor.execute(sql, val)
  mydb.commit()

  # Esperar 5 segundos
  time.sleep(5)


    