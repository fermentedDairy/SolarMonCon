from umqtt.simple import MQTTClient
import config
import constants


class MyMQTT:
    __client = None
    __BATTERY_STATE_TOPIC = b'solar_assistant/total/battery_state_of_charge/state'
    __BATTERY_POWER_STATE_TOPIC = b'solar_assistant/total/battery_power/state'
    
    __GRID_VOLTAGE_STATE_TOPIC = b'solar_assistant/inverter_1/grid_voltage/state'
    
    __CHARGER_SOURCE_PRIORITY_TOPIC = b'solar_assistant/inverter_1/charger_source_priority/state'
    __OUTPUT_SOURCE_PRIORITY_TOPIC = b'solar_assistant/inverter_1/output_source_priority/state'
    
    __CHARGER_SOURCE_PRIORITY_SET_TOPIC = b'solar_assistant/inverter_1/charger_source_priority/set'
    __OUTPUT_SOURCE_PRIORITY_SET_TOPIC = b'solar_assistant/inverter_1/output_source_priority/set'
    

    
    __topics = [__BATTERY_STATE_TOPIC,
                __CHARGER_SOURCE_PRIORITY_TOPIC,
                __OUTPUT_SOURCE_PRIORITY_TOPIC,
                __BATTERY_POWER_STATE_TOPIC,
                __GRID_VOLTAGE_STATE_TOPIC]
    
    __topics_value_map = {}
    
    def receive(self, topic, msg):
        self.__topics_value_map[topic] = msg.decode("utf-8") 
        
    
    def configure(self):
        self.__client = MQTTClient('SolarMonMain', config.UMQTT_HOST, config.UMQTT_PORT, config.UMQTT_USER, config.UMQTT_PASS)
        self.__client.set_callback(self.receive)
        self.__client.connect()
        print('Connected to MQTT Broker')
        for topic in self.__topics:
            print("Subscribing to ", topic)
            self.__client.subscribe(topic)
        
    def check_msg(self):
        self.__client.check_msg()
        
    def get_battery_percentage(self):
        return self.__topics_value_map.get(self.__BATTERY_STATE_TOPIC, 999)
    
    def get_output_source_priority(self):
        return self.__topics_value_map.get(self.__OUTPUT_SOURCE_PRIORITY_TOPIC, constants.UNKNOWN)
    
    def get_charger_source_priority(self):
        return self.__topics_value_map.get(self.__CHARGER_SOURCE_PRIORITY_TOPIC, constants.UNKNOWN)
    
    def get_grid_voltage(self):
        return float(self.__topics_value_map.get(self.__GRID_VOLTAGE_STATE_TOPIC, '0'))
    
    def get_battery_power_state(self):

        return float(self.__topics_value_map.get(self.__BATTERY_POWER_STATE_TOPIC, '0'))
    
    def set_output_source_priority(self, value):
        print("publishing to ", self.__OUTPUT_SOURCE_PRIORITY_SET_TOPIC, ", value ", value)
        self.__client.publish(self.__OUTPUT_SOURCE_PRIORITY_SET_TOPIC, value)
    
    def set_charger_source_priority(self, value):
        print("publishing to ", self.__CHARGER_SOURCE_PRIORITY_SET_TOPIC, ", value ", value)
        self.__client.publish(self.__CHARGER_SOURCE_PRIORITY_SET_TOPIC, value)
        