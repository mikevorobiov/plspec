#import pyvisa
from numpy.random import randn
from numpy import sqrt
import mono

class Daq(mono.Mono):
    daq_visa = []
    integration_time = super().integration_time

    def __init__(self):
        self.connect()
        return 0

    def connect(self):
        print('Whoa! Connection established!')
        return 0

    def get_reading(self):
        if self.integration_time > 0.0:
            return randn() / sqrt(self.integration_time)
        else:
            return randn()
