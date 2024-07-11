"""
    Práctica 06: Raspberry Pi (sincronización de tiempo)

    Equipo 07
        Castro Cazares Carlos Jahir (Responsable)
        Vieyra Ernesto

    Objetivo: Sincronizar el tiempo de una Raspberry Pi.

    ####################################################
    Python v3.8
    Instalacion de librerias
        NTPLIB => pip install ntplib
"""

# Librerias
import datetime
from time import ctime
import ntplib
import os

if __name__ == '__main__':
    #Hora del Cliente
    print('Tiempo actual del cliente: ' + str(datetime.datetime.now()))

    # Hora cuando se hiso emvio la peticion
    horaEnvio = datetime.datetime.now()
    print('___________________________________________________________________')
    print('Hora de envio de la peticion: '+str(horaEnvio))

    # Peticion al servidor
    print('___________________________________________________________________')
    servidor = 'time-e-g.nist.gov'
    clienteNTP = ntplib.NTPClient()
    request = clienteNTP.request(servidor)
    fechaServidor = datetime.datetime.strptime(ctime(request.tx_time), "%a %b %d %H:%M:%S %Y")
    print("Respuesta de "+servidor+": "+str(fechaServidor))

    # Hora de llegada
    horaLlegada = datetime.datetime.now()
    print('___________________________________________________________________')
    print('Hora de llegada de la peticion: ' + str(horaLlegada))

    # Retraso
    retraso = ((horaLlegada - horaEnvio)/2)
    print('___________________________________________________________________')
    print('Retraso: ' + str(retraso))

    # Hora real
    horaReal = fechaServidor + retraso
    print('___________________________________________________________________')
    print('Hora de real (Calculada): ' + str(horaReal))

    # Cambiar la hora del dispositivo
    print('___________________________________________________________________')
    print('Cambio de hora por el sistema')
    os.system('sudo date --set="'+str(horaReal)+'"  && date --rfc-3339=ns')
