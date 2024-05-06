#This file was created by Nathan and Ryan to communicate with the spectrometer and collect and store absorption data.
#These lines below import the necessary objects and definitions needed for the code.
from genesys import Genesys
import time
import csv
import pandas as pd
import serial

def sleep(seconds):
    time.sleep(seconds)

#Nathan - This code block communicates with the spectrometer by telling it when to beep, before and after blanking, how long to sleep for, and when to begin reading absorbance.
spectrometer = Genesys("COM3")
spectrometer.wavelength(wl=500)
spectrometer.beep()
spectrometer.blank()
spectrometer.beep(times=3)
time.sleep(6)
spectrometer.beep()
spectrometer.reading()


#Ryan- This line calls for the start time to begin as whatever the time is.
start_time = time.time()

#Ryan- These lines create the objects for data to be saved to accordingly.
time_data = []
absorbance_data = []

#Ryan- This block defines the function needed to read absorption data from the spectrometer and store the data as a float.
def read_spectrometer_data():
    ser = spectrometer
    ser.reading()
    response = ser.readline().decode('utf-8').strip()
    absorbance = float(response)

    return absorbance

#Ryan- This block creates a loop for 10 seconds that collects data and saves the data to the appropriate object and save it to a csv file.
while time.time() - start_time < 10:
    absorbance = spectrometer.reading() 
    current_time = time.time() - start_time
    print(current_time)
    time_data.append(current_time)
    absorbance_data.append(absorbance)
    time.sleep(1)
df = pd.DataFrame({'Time': time_data, 'Absorbance': absorbance_data})
df.to_csv('computingdata.csv', index=False)

spectrometer.beep()
