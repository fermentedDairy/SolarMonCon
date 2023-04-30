import network
import config
import utime
from LED import toggle_led
from FourDigitSevenSegment import FourDigitSevenSegment

class MyWifi:
    __wlan = None
    __display = FourDigitSevenSegment()
    
    def get_wifi(self):
        return self.__wlan
        
    def logon_to_network(self):
        print("logging on to network")
        self.__wlan = network.WLAN(network.STA_IF)
        self.__wlan.active(True)
        self.__wlan.config(pm = 0xa11140) # Diable powersave mode
        self.__wlan.connect(config.SSID, config.PASSWORD)
        
        max_wait = 10
        while max_wait > 0:
            self.__display.display_number('A   ')
            if self.__wlan.status() < 0 or self.__wlan.status() >= 3:
                break
            max_wait -= 1
            print('waiting for connection...')
            toggle_led("LED")
            utime.sleep(1)
            