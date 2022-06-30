import numpy as np
from spectrum import Spectrum

class Mono:
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

    current_reading = 0.0
    current_position = 0.0
    current_in_slit = 0.1
    current_out_slit = 0.1
    current_grating = 0

    wavelength_start = 0.0
    wavelength_stop = 0.0
    wavelength_step = 2.0

    grating_types = {'1200': 0, '900': 1}