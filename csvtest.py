from genesys import Genesys
import serial
import csv
import pandas as pd

ser = serial.Serial('COM3', 9600)

with open('computingdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "Absorbance"])
    while True:
        data = ser.readline().decode('utf-8').rstrip()
        if data:
            time, absorbance = data.split(',')
            writer.writerow([time, absorbance])

ser.close()
