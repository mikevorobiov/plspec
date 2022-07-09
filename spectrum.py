import numpy as np
from mono import Mono
from ui_main_window import Ui_MainWindow

class Spectrum(Ui_MainWindow):
    '''
    Spectrum class encapsulates raw data as
        - wavelength samples in the 'wavelength' numpy array
        - the corresponding intensity readings in the 'intensity_raw' numpy array
    and the processed data that includes
        - energy samples calculated as $E=hc/\lambda=1239.8/\lambda$ stored in 'energy' array
        - intensity readings divided by the spectral response function of the optical system stored in 'intensity_corrected'
        - the spectral response is stored in 'spectral_response' array
    Python 3.10 was used at the time it was written.
    '''
    is_inporgress = False
    is_corrected = False
    is_xshifted = False
    is_scaled = False
    is_saved = False
    is_shown = False
    is_empty = True

    id = ''
    number = 0
    saving_prefix = ''
    saving_columns = ['wl', 'e', 'intensity', 'corrections', 'spectrum', 'wshifted', 'scaled']

    nsamples = 0
    step = 0.0
    eshift = 0.0
    wshift = 0.0
    scale = 1.0
    
    integration_time = 0.0              # Integration time of the DAQ (sec)
    in_slit = 0.1                       # Monochromator input slit width in (mm)
    out_slit = 0.1                      # Monochromator output slit width in (mm)
    excitation_intensity = 0.0          # Laser excitation intensity (W/cm2)
    temperature = 0.0                   # Sample temperature in absolute units (Kelvin)
    correction_index = 0                # Index that represents proper correction curve

    wavelength = []                     # Wavelngth sampling positions (nm)
    wavelength_shifted = []
    intensity_raw = []                  # PL intensity raw measurements (counts)
    background = []                     # Background parasitic counts if needed (counts)

    energy = []                         # Energy sampling positions (eV)
    energy_shifted = [] 
    intensity_corrected = []            # PL intensity corrected samples in units proportional to spectal photon flux (counts/(sec*nm))
    intensity_scaled = []   

    calibration_curve = []
    spectral_response = []              # Spectral response function of the experimental setup (counts)


    def __init__(self):
        self.step = super().wavelength_step
        self.integration_time = super().integration_time

    def load_calibration(self):
        try:
            self.calibration_curve = np.genfromtxt('calibration_curve.csv', delimiter=',')
            print('Calibration curve successfuly loaded!')
        except:
            print('Error: Couldn\'t load calibration curve from a file.')
        # Further resample curve according to self.wavelength
        return 0

    def recalibrate(self):
        self.intensity_corrected = self.intensity_raw * self.wavelength**3 / (self.in_slit**2 * self.excitation_intensity * self.spectral_response)
        return 0

    def append_reading(self):
        x = super().current_position
        y = super().current_reading

        x_cal = self.calibration_curve[:,0]
        y_cal = self.calibration_curve[:,1]
        cal = np.interp(x, x_cal, y_cal)

        y_corrected = y * x**3 / (self.in_slit**2 * self.excitation_intensity * cal)

        self.wavelength = np.append(self.wavelength, x)
        self.wavelength_shifted = np.append(self.wavelength, x + self.wshift)
        self.energy = np.append(self.wavelength, 1239.8/x)
        self.energy_shifted = np.append(self.wavelength, 1239.8/(x + self.wshift))

        self.spectral_response = np.append(self.spectral_response, cal)
        self.intensity_raw = np.append(self.intensity_raw, y)
        self.intensity_corrected = np.append(self.intensity_corrected, y_corrected)
        self.intensity_scaled = np.append(self.intensity_scaled, y_corrected * self.scale)

        self.nsamples += 1
        return 0
  
    def get_wavelength(self):
        return self.wavelength

    def get_wavelength_shifted(self):
        return self.wavelength_shifted

    def get_energy(self):
        return self.energy

    def get_energy_shifted(self):
        return self.energy_shifted

    def get_raw(self):
        return self.intensity_raw

    def get_corrected(self):
        return self.intensity_corrected
    
    def get_scaled(self):
        return self.intensity_scaled

    def get_background(self):
        return self.background

    def set_id(self, id=''):
        self.id = id
        return 0

    def set_number(self, number=0):
        self.number = number
        return 0

    def show(self):
        return 0

    def save(self):
        return 0
