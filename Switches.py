from machine import Pin
import constants

class Switches:

    __SBU = Pin(20, Pin.IN, Pin.PULL_DOWN)
    __SUB = Pin(21, Pin.IN, Pin.PULL_DOWN)
    __SOLAR_FIRST = Pin(22, Pin.IN, Pin.PULL_DOWN)
    __SOLAR_UTILITY = Pin(26, Pin.IN, Pin.PULL_DOWN)
    
    def get_output_priority(self):
        if self.__SBU.value():
            return constants.SBU
        elif self.__SUB.value():
            return constants.SUB
        else:
            return constants.UNKNOWN
    
    def get_charge_priority(self):
        if self.__SOLAR_FIRST.value():
            return constants.SOLAR_FIRST
        elif self.__SOLAR_UTILITY.value():
            return constants.SOLAR_UTILITY
        else:
            return constants.UNKNOWN
    
