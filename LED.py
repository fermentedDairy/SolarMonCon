from machine import Pin
import constants

__SBU = 16
__SUB = 17
__SOLAR_FIRST = 18
__SOLAR_UTILITY = 19

def turn_led_on(pin):
    Pin(pin, Pin.OUT).high()

def turn_led_off(pin):
    Pin(pin, Pin.OUT).low()

def toggle_led(pin):
    Pin(pin, Pin.OUT).toggle()
    
def set_sbu():
    turn_led_off(__SUB)
    turn_led_on(__SBU)

def set_sub():
    turn_led_off(__SBU)
    turn_led_on(__SUB)
    
def clear_sbu_sub():
    turn_led_off(__SBU)
    turn_led_off(__SUB)
        
def set_solar_first():
    turn_led_off(__SOLAR_UTILITY)
    turn_led_on(__SOLAR_FIRST)
        
def set_solar_utility():
    turn_led_off(__SOLAR_FIRST)
    turn_led_on(__SOLAR_UTILITY)

def clear_solar_utility_first():
    turn_led_off(__SOLAR_FIRST)
    turn_led_off(__SOLAR_UTILITY)
    
def set_indicators(mqtt):
    output_source_priority = mqtt.get_output_source_priority()
    charger_source_priority = mqtt.get_charger_source_priority()
    
    if output_source_priority == constants.SBU:
        set_sbu()
    elif output_source_priority == constants.SUB:
        set_sub()
    else:
        clear_sbu_sub()
        
    if charger_source_priority == constants.SOLAR_FIRST:
        set_solar_first()
    elif charger_source_priority == constants.SOLAR_UTILITY:
        set_solar_utility()
    else:
        clear_solar_utility_first()
