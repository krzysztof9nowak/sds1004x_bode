'''
Created on Apr 24, 2018

@author: 4x1md
'''

import serial
import time
from awgdrivers.base_awg import BaseAWG
from . import constants
from awgdrivers.exceptions import UnknownChannelError

AWG_ID = "sna"

class SnaAWG(BaseAWG):
    '''
     Use my scalar network analyzer as waveform generator
    '''
    
    SHORT_NAME = "sna"

    def __init__(self, port, *args):
        self.port = port
    
    def connect(self):
        self.ser = serial.Serial(port=self.port, baudrate=115200)
    
    def disconnect(self):
        self.ser.close()
    
    def initialize(self):
        self.connect()
        self.set_amplitue(None, 10)
    
    def get_id(self):
        return AWG_ID
    
    def enable_output(self, channel, on):
        pass
    
    def set_channel(self, chn):
        pass
    
    def set_output(self, on=False):
        pass
    
    def set_frequency(self, channel, freq):
        self.ser.write(F"f{float(round(freq,0))}\n".encode('ASCII'))
        time.sleep(0.001)
        
    def set_phase(self, phase):
        pass

    def set_wave_type(self, channel, wvtp):
        pass
    
    def set_amplitue(self, channel, ampl):
        R_set = 39.93 * (2.0 * 50.0 * 470.0 / 200.0) / ampl
        R_pot = R_set - 1800
        value = (R_pot / 50e3) * 127
        value = int(max(min(value, 127), 0))
        # print(value)
        self.ser.write(F"a{value}\n".encode('ASCII'))
        time.sleep(0.001)
        
    
    def set_offset(self, channel, offset):
        pass
    
    def set_load_impedance(self, channel, z):
        pass
    
