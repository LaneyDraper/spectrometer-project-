from genesys import Genesys
import time

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
