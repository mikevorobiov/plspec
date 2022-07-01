import numpy as np
from spectrum import Spectrum
from daq import Daq

class Mono(QApp):
    '''
    Abstraction class for a Cornerstone 260 monochromator 
    control. It requires cornerstone.dll (win32) library
    which exsits under win32 only.
    The program must be run inder win32 version of python.
    Python 3.10 was used at the time it was written. 
    '''
    is_connected = False
    is_busy = False

    query_str = 'Query string is empty...'

    current_reading = 1.0e-10
    current_position = 0.0
    current_in_slit = 0.1
    current_out_slit = 0.1
    current_grating = 0

    wavelength_start = 0.0
    wavelength_stop = 0.0
    wavelength_step = 2.0

    grating_types = {'1200': 0, '900': 1}

    integration_time = 0.5

    daq = Daq()

    def __init__(self):
        return 0

    def connect(self):
        try:
            print('Trying to connect to Cornerstone 260 monochromator...')

            self.is_connected = True
            print('Succesfuly connected to the monochromator!')
        except:
            self.is_connected = False
            print('Error: Couldn\'t connect to the monochromator.\n\tTroubleshoot and try again!')
        return 0

    def query(self):
        return 0
    
    def get_position(self):
        return 0

    def get_grating(self):
        return 0

    def command(self):
        return 0

    def goto(self):
        return 0
    
    def set_grating(self):
        return 0

    def scan(self):
        self.is_busy = True
        return 0

    def abort_scan(self):
        return 0