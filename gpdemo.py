import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
ok=False
stop=0
try:
    while ok==False:
        try:
            data = ser.readline()
        except:
            stop=stop+1
            if stop==10000:
                break
#wait for the serial port to churn out data
        if data[0:6] == '$GPGGA': # the long and lat data are always contained in the GPGGA string of the NMEA data

            msg = pynmea2.parse(data)
            latval = msg.lat #parse the latitude and print
            concatlat = str(latval)
            try:           
                minutos_lat = str(float(concatlat[2:])/60)
            except:
                minutos_lat = '0' 
            latitud = concatlat[0:2] + minutos_lat[1:]
            #print(concatlat)
            #print(latitud)

           #parse the longitude and print
            longval = msg.lon
            concatlong = str(longval)
            grados_longitud = str(int(concatlong[1:3])*(-1))
            try: 
                minutos_long = str(float(concatlong[2:])/60)
            except:
                minutos_long='0'
            longitud = grados_longitud + minutos_long[2:]
            #print(concatlong)
            #print(longitud)

            print('-lat '+latitud+' -lon '+longitud)
            ok=True
            time.sleep(0.5) #wait a little before picking the next data.

except KeyboardInterrupt:
    time.sleep(2)
