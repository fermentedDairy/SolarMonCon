from FourDigitSevenSegment import FourDigitSevenSegment
from LED import turn_led_on, turn_led_off, set_indicators, toggle_led
from WiFi import MyWifi
from mqttClient import MyMQTT
from Switches import Switches
from machine import Pin, reset
import constants
import time
import config

i = 0
while i <= 5:
    time.sleep(0.5)
    toggle_led("LED")
    i = i + 1
    
wifi = MyWifi()
mqtt = MyMQTT()
switches = Switches()
display = FourDigitSevenSegment()

# Poll the switch pins. Only publish if desired and current are different. wait 1000 loops to prevent interface flooding
def publish_output_if_required(count):
    current_output_source_priority = mqtt.get_output_source_priority()
    desired_output_source_priority = switches.get_output_priority()

    if desired_output_source_priority == constants.UNKNOWN or current_output_source_priority == constants.UNKNOWN:
        return 0

    if current_output_source_priority == desired_output_source_priority:  # the same, don't so anything      
        return 0
    elif count == 0:  # not the same and count is 0, publish desired
        print("current: ", current_output_source_priority, "; desired: ", desired_output_source_priority)
        mqtt.set_output_source_priority(desired_output_source_priority)
        return 10000
    else:
        return count - 1  # count down


def publish_charger_if_required(count):
    current_charger_source_priority = mqtt.get_charger_source_priority()
    desired_charger_source_priority = switches.get_charge_priority()

    if desired_charger_source_priority == constants.UNKNOWN or current_charger_source_priority == constants.UNKNOWN:
        return 0

    if current_charger_source_priority == desired_charger_source_priority:  # the same, don't so anything
        return 0
    elif count == 0:  # not the same and count is 0, publish desired
        print("current: ", current_charger_source_priority, "; desired: ", desired_charger_source_priority)
        mqtt.set_charger_source_priority(desired_charger_source_priority)
        return 10000
    else:
        return count - 1  # count down


turn_led_off("LED")

wifi.logon_to_network()
print("WiFi Status:", str(wifi.get_wifi().status()))
if wifi.get_wifi().status() != 3:
    i = 0
    while i <= 100:
        display.display_number('A  ' + str(wifi.get_wifi().status()))
        i = i + 1
    reset()
    
turn_led_on("LED")

try:
    mqtt.configure()
except:  # NOSONAR; python:S5754; The docs don't mention an exception type, I'm ignoring the linter
    print('Could not connect to mqtt. Resetting')
    i = 0
    while i <= 100:
        display.display_number("C    ")
        i = i + 1
    reset()

print("startup complete")
output_count = 0
charger_count = 0
    
while True:
    mqtt.check_msg()
    set_indicators(mqtt)
    display.display_number(mqtt.get_battery_voltage())
    output_count = publish_output_if_required(output_count)
    charger_count = publish_charger_if_required(charger_count)
    display.display_number(mqtt.get_battery_voltage())
