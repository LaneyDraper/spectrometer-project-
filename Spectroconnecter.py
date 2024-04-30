from genesys import Genesys

spectrometer = Genesys("COM3")
spectrometer.wavelength(wl=500)
spectrometer.beep()
spectrometer.blank()
spectrometer.beep(times=3)
spectrometer.reading()
