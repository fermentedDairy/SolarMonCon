import network
import config
import utime
from LED import turn_led_on, toggle_led

class MyWifi:
    __wlan = None
    
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
            if self.__wlan.status() < 0 or self.__wlan.status() >= 3:
                break
            max_wait -= 1
            print('waiting for connection...')
            toggle_led("LED")
            utime.sleep(1)
            
            #Handle connection error
            print(self.__wlan.status())
            if self.__wlan.status() != 3:
                raise RuntimeError('wifi connection failed')
            else:
                turn_led_on("LED")
                print('connected')
                status = self.__wlan.ifconfig()
                print('ip = ' + status[0])