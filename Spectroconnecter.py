from genesys import Genesys
import time
import csv
import pandas as pd
import serial

def sleep(seconds):
    time.sleep(seconds)
    
spectrometer = Genesys("COM3")
spectrometer.wavelength(wl=500)
spectrometer.beep()
spectrometer.blank()
spectrometer.beep(times=3)
time.sleep(6)
spectrometer.beep()
spectrometer.reading()

start_time = time.time()

time_data = []
absorbance_data = []

def read_spectrometer_data():
    ser = spectrometer
    ser.reading()
    response = ser.readline().decode('utf-8').strip()
    absorbance = float(response)

    return absorbance

start_time = time.time()

while time.time() - start_time < 10:
    absorbance = spectrometer.reading() 
    current_time = time.time() - start_time
    print(current_time)
    time_data.append(current_time)
    absorbance_data.append(absorbance)
    time.sleep(0.01)
df = pd.DataFrame({'Time': time_data, 'Absorbance': absorbance_data})
df.to_csv('computingdata.csv', index=False)

spectrometer.beep()
