#import pyvisa
from mono import Mono

class Daq(Mono):
    daq_visa = []
    integration_time = super().integration_time

    def __init__(self):
        self.connect()
        return 0

    def connect(self):
        return 0

    def get_reading(self):
        return 0
