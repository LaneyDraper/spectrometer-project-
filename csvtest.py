from genesys import Genesys
import serial
import csv
import pandas as pd
import time

with open("computingdata.csv", "r", newline='') as csvfile:
    header = csvfile.readline().strip()

with open ("computingdata.csv", "w", newline='') as csvfile:
    csvfile.write(header + "\n")
    
ser = serial.Serial("COM3", 9600)

with open("computingdata.csv", "a", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "Absorbance"])
    start_time = time.time()
    while time.time() - start_time < 30:
        data = ser.readline().decode("utf-8").rstrip()
        if data:
            time, absorbance = data.split(',')
            writer.writerow([time, absorbance])
        time.sleep(3)

ser.close()

for i in range(30):
    df = pd.read_csv("computingdata.csv")
    print(df)
    time.sleep(1)
