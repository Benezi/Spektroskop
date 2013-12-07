import serial
import array
import threading
import time
import datetime
import os
import sys


class Measurement():
    '''This is an fork of spektroskop.py to show benedikt, how to use classes in his context.'''

    pfad = os.path.abspath(".") + "\DATA\\"

    def __init__(self):
        '''even can call: self._prepare_test()'''
        self.prepare_com_port()
        self.prepare_path()
        self.get_title()

    def _prepare_test(self):
        '''!Contains all methods which are needed to start and prepared measurement.'''
        self.prepare_com_port()
        self.prepare_path()
        self.get_title()

    def prepare_com_port(self):
        port = input("COM-Port: ")
        w = 1
        while w:
            try:
                self.ser = serial.Serial("Com" + port,19200,timeout=0)
                w = 0
            except:
                print("Fehler bei Verbindung!")
                port = input("COM-Port: ")
                w = 1

    def prepare_path(self):
        try:
            if not os.path.isdir(self.pfad):
                os.mkdir(self.pfad)
        except:
            a = input("Fehler beim Zugriff auf Pfad")
            sys.exit()

    def get_title(self):
        self.titel = input("Titel der Messreihe: ")
        w = 1
        while w:
            try:
                fobj_out = open(self.pfad + self.titel + ".csv","a")
                fobj_out.write("SPEKTROSKOPIE")
                fobj_out.close()
                print("Spektroskopie wird gespeicher unter: \n" + self.pfad + self.titel + ".csv")
                w = 0
            except:
                print("Fehler beim Zugriff auf Datei")
                self.titel = input("Anderer Dateiname: ")
                w = 1

    def start_measurement(self):

        liste = array.array('I',(0,)*256)
        print("Beginn der Messung: " + time.strftime("%d.%m.%Y um %H:%M:%S Uhr"))
        zeit_beginn = datetime.datetime.today()

        while 1:
            if self.ser.inWaiting() > 0:
                while self.ser.inWaiting() > 0:
                    x = self.ser.read()
                    z = ord(x)
                    liste[z] = liste[z] + 1
                fobj_out = open(self.pfad + self.titel + ".csv","w")
                fobj_out.write("Messdauer;" + str(datetime.datetime.today() - zeit_beginn) + '\n')
                for i in range(256):
                    fobj_out.write(str(i) + ";" + str(liste[i]) + '\n')
                fobj_out.close()


if __name__ == "__main__":
    measurement = Measurement() #It calls the __init__-method and makes the preparation with the 3 encapsulated functions.
    measurement.start_measurement() # now we call the start_measurement method explicit.
