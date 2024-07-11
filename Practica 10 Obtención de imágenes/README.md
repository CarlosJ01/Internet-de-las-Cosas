# Práctica 10: Obtención de imágenes
**Objetivo:** Obtener imágenes de una cámara
**Equipo 7:**
- Castro Cazares Carlos Jahir (Responsable) 	
- Vieyra Ernesto
**Programado y Probado en Windows 10**

# Configuración
***Version***
Python 3.8.8

***Librerías***
Instalar las siguiente librerías de python:
 - OpenCV => pip install opencv-python 
 - Requests => pip install requests

***Instalación de Base de Datos***
Tendrá que crear la base de datos donde se guardaran las fotos del cliente en el servidor con el script de **bd_camara.sql**, la base de datos será en el servidor.

***Instalar en el Servidor HTTP***
 - Poner el contenido de la carpeta **Cliente**, en el servidor apache
   del cliente.
 - Poner el contenido de la carpeta **Servidor**, en el    servidor
   apache del servidor.

***Direcciones URL del  servidor y cliente y tiempo de tomar foto***
En el archivo de **camara.py** del cliente las siguientes variables:
 - Poner en la variable **urlServidor (Linea 18)**, la URL del archivo
   */php/recibirImagen.php* del servidor apache del servidor, con su ip; Ejemplo "http://192.168.100.15/IOT/P10S/php/recibirImagen.php".
 - Poner en la variable **urlCliente(Linea 19)**, la URL de la carpeta
   del cliente apache del cliente, con la ip del cliente; Ejemplo
   "http://192.168.100.16/IOT/P10C/"

***Conexión con la Base de Datos***
En el archivo **php\conexionSQL.php** del servidor cambiar las siguientes líneas para configurar la conexión de la base de datos; Cambiar las lineas **$conexion =  mysqli_connect("localhost",  "root",  "",  "camara",  3307); Linea 3 y 14**, donde la configuracion es host, usuario, password, base_datos, puerto.

***Tiempo de recarga y tomar foto***
 - En el archivo de **camara.py** del cliente cambiar el valor numérico
   de la linea **time.sleep(1) (Linea 46)**,    para cambiar el tiempo
   de espera entre foto y foto en segundos.
 - En el archivo de **js\getImagenes.js** del servidor, cambiar la
   **linea 27**, al tiempo de recarga de la ultima imagen en milisegundos.

# Correr Practica
Abrir en el navegador el servidor Apache del servidor por Ejemplo: http://localhost/IOT/P10S/, posteriormente en el cliente correr el archivo **camara.py**. Y en el navegador se mostrara la imagen mas reciente con un atraso de 1 segundo y toma la imagen cada segundo.