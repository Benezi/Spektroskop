import serial
from time import gmtime, strftime
import time
import sys
import os
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

titel = input("Titel der Messreihe: ")
w = 1
while w:
    try:
        fobj_out = open(pfad + titel + ".csv","a")
        fobj_out.write("LOG\n")
        fobj_out.close()
        print("Log wird gespeicher unter: \n" + pfad + titel + ".csv")
        w = 0
    except:
        print("Fehler beim Zugriff auf Datei")
        titel = input("Anderer Dateiname: ")
        w = 1
#----------------------------------------------------------------
intervall = input("Intervall: ")
#----------------------------------------------------------------
print("Beginn der Messung: " + time.strftime("%d.%m.%Y um %H:%M:%S Uhr"))
z = 0
#----------------------------------------------------------------
while 1:
    sys.stdout.flush()
    time.sleep(float(intervall))
    while ser.inWaiting() > 0:
            x = ser.read()
            z = z + 1
    fobj_out = open(pfad + titel + ".csv","a")
    fobj_out.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ";" + str(z) + '\n')
    fobj_out.close()
    z = 0
