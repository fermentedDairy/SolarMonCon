import ujson

f = open('config.json', 'r')
config = ujson.load(f)
print("config: ", config)

SSID = config['WIFI']['SSID']
PASSWORD = config['WIFI']['PASSWORD']

UMQTT_HOST = config['UMQTT']['HOST']
UMQTT_PORT = config['UMQTT']['PORT']
UMQTT_USER = config['UMQTT']['USER']
UMQTT_PASS = config['UMQTT']['PASS']