
import numpy as np

class Mono:
    '''
    Abstraction class for a Cornerstone 260 monochromator 
    control. It requires cornerstone.dll (win32) library
    which exsits under win32 only.
    The program must be run inder win32 version of python.
    Python 3.10 was used at the time it was written. 
    '''
    isactive = False
    query_str = 'Empty'