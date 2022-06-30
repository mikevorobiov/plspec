import numpy as np
from mono import Mono

class Spectrum(Mono):
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
    is_corrected = False
    is_xshifted = False
    is_scaled = False
    is_saved = False

    saving_prefix = ''
    saving_columns = ['wl', 'e', 'intensity', 'corrections', 'spectrum']

    nsamples = 0
    step = 0.0
    xshift = 0.0
    scale = 1.0
    
    integration_time = 0.0              # Integration time of the DAC (sec)
    in_slit = 0.1                       # Monochromator input slit width in (mm)
    out_slit = 0.1                      # Monochromator output slit width in (mm)
    excitation_intensity = 0.0          # Laser excitation intensity (W/cm2)
    temperature = 0.0                   # Sample temperature in absolute units (Kelvin)
    correction_index = 0                # Index that represents proper correction curve

    wavelength = np.empty()             # Wavelngth sampling positions (nm)
    intensity_raw = np.empty()          # PL intensity raw measurements (counts)
    background = np.empty()             # Background parasitic counts if needed (counts)

    energy = np.empty()                 # Energy sampling positions (eV)
    intensity_corrected = np.empty()    # PL intensity corrected samples in units proportional to spectal photon flux (counts/(sec*nm))
    spectral_response = np.empty()      # Spectral response function of the experimental setup (counts)



    self._init_(self):
        return 0

    self.calibrate(self):
        return 0

    self.get_raw(self):
        return 0

    self.get_corrected(self):
        return 0

    self.save(self):
        return 0
