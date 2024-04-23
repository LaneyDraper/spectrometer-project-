#!/usr/bin/env python3.4

# This file defines a class Genesys that extends the Serial class of pySerial
# to provide methods for interacting with a Genesys visible spectrophotometer.
# The program will also (eventually) provide a program to interact with a
# spectrophotometer using a minimal console interaction.

from serial import Serial

class Genesys(Serial):
    """Wraps a serial port instantiation with methods to adjust settings
    and read data from a Genesys visible spectrophotometer. Class instantiation
    needs to specify the serial port to which the spectrophotometer is attached
    as a string."""
    def gwrite(self, input):
        """Writes the provided string to the spectrophotometer in an appropriate
        format, and reads the returned output from the spectrophotometer until
        it is ready for additional input (marked by an OK message)."""
        self.write(bytes('{}\r\n'.format(input), 'us-ascii'))
        for x in range(10):   # Prevent an endless loop.
            output = self.readline()
            if 'OK' in output.decode():
                break
        return
    def gread(self, input):
        """Writes the provided string to the spectrophotometer in an appropriate
        format, and reads the returned output from the spectrophotometer until
        it is ready for additional input (marked by an OK message). The line
        returned before the OK message is stripped and returned."""
        self.write(bytes('{}\r\n'.format(input), 'us-ascii'))
        previous = ''
        for x in range(10): # Prevent an endless loop.
            next = self.readline().decode().strip()
            if 'OK' in next:
                break
            else:
                previous = next
        return previous
    def absorbance(self, absorb=None):
        """Sets the absorbance to the value specified as an argument, or sets
        the spectrometer to absorbance mode if no argument is supplied."""
        if absorb is None:
            self.gwrite('ABS')
        else:
            if (absorb >= 0) and (absorb <= 2.5):
                self.gwrite('ABS {:.3}'.format(absorb))
            else:
                raise ValueError('Absorbance must be between 0 and 2.5')
        return
    def reading(self):
        """Collects a reading from the spectrophotometer."""
        return float(self.gread('SND'))
    def blank(self):
        """Sets the spectrophotometer to zero absorbance (100% transmittance).
        The blank should be in the spectrophotometer when this is used."""
        self.gwrite('ZER')
        return
    def beep(self, times=1):
        """Tells the instrument to beep a specified number of times."""
        if isinstance(times, int) and (times >= 1) and (times <= 3):
            self.gwrite('BEP {}'.format(times))
        else:
            raise ValueError("Argument must be an integer between 1 and 3.")
        return
    def wavelength(self, wl=None):
        """Sets the wavelength of the spectrophotometer to the supplied
        value, or returns the wavelength to which it is already set."""
        if wl is None:
            return int(self.gread('GTO'))
        else:
            if isinstance(wl, int) and (wl>=325) and (wl<=1100):
                self.gwrite('GTO {}'.format(wl))
                return
            else:
                raise ValueError("Wavelength must be an integer between 325 and 1100.")

