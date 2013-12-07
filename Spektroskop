import serial
import array
import threading
import time
import datetime
import os
import sys
#----------------------------------------------------------------
port = input("COM-Port: ")
w = 1
while w:
    try:
        ser = serial.Serial("Com" + port,19200,timeout=0)
        w = 0
    except:
        print("Fehler bei Verbindung!")
        port = input("COM-Port: ")
        w = 1
#----------------------------------------------------------------
try:
    pfad = os.path.abspath(".") + "\DATA\\"
    if not os.path.isdir(pfad):
        os.mkdir(pfad)
except:
    a = input("Fehler beim Zugriff auf Pfad")
    sys.exit()

#----------------------------------------------------------------
titel = input("Titel der Messreihe: ")
w = 1
while w:
    try:
        fobj_out = open(pfad + titel + ".csv","a")
        fobj_out.write("SPEKTROSKOPIE")
        fobj_out.close()
        print("Spektroskopie wird gespeicher unter: \n" + pfad + titel + ".csv")
        w = 0
    except:
        print("Fehler beim Zugriff auf Datei")
        titel = input("Anderer Dateiname: ")
        w = 1
#----------------------------------------------------------------
liste = array.array('I',(0,)*256)
print("Beginn der Messung: " + time.strftime("%d.%m.%Y um %H:%M:%S Uhr"))
zeit_beginn = datetime.datetime.today()

while 1:
    if ser.inWaiting() > 0:
        while ser.inWaiting() > 0:
            x = ser.read()
            z = ord(x)
            liste[z] = liste[z] + 1
        fobj_out = open(pfad + titel + ".csv","w")
        fobj_out.write("Messdauer;" + str(datetime.datetime.today() - zeit_beginn) + '\n')
        for i in range(256):
            fobj_out.write(str(i) + ";" + str(liste[i]) + '\n')
        fobj_out.close()
