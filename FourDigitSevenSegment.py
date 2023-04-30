from machine import Pin
import time


def clear_segment_pins():
    for pin in range(4, 11):
        Pin(pin, Pin.OUT).low()


class FourDigitSevenSegment:

    # https://circuitdigest.com/sites/default/files/inlineimages/Seven-Segment-Display.gif
    # Pin to segment map
    __A = Pin(4, Pin.OUT)
    __B = Pin(5, Pin.OUT)
    __C = Pin(6, Pin.OUT)
    __D = Pin(7, Pin.OUT)
    __E = Pin(8, Pin.OUT)
    __F = Pin(9, Pin.OUT)
    __G = Pin(10, Pin.OUT)


    __num_to_pin_map = {' ': (),
                        '0': (__A, __B, __C, __D, __E, __F),
                        '1': (__B, __C),
                        '2': (__A, __B, __G, __E, __D),
                        '3': (__A, __B, __G, __C, __D),
                        '4': (__F, __G, __B, __C),
                        '5': (__A, __F, __G, __C, __D),
                        '6': (__A, __F, __E, __D, __C, __G),
                        '7': (__A, __B, __C, __F),
                        '8': (__A, __B, __C, __D, __E, __F, __G),
                        '9': (__F, __A, __B, __G, __C, __D),
                        'A': (__A, __B, __C, __G, __E, __F),
                        'C': (__A, __F, __E, __D)}

    def print_7_seg_number(self, index, digit):
        clear_segment_pins()
        for pin in range(0, 4):
            if pin != index:
                Pin(pin, Pin.OUT).high()
            else:
                Pin(pin, Pin.OUT).low()

        for pin in self.__num_to_pin_map[digit]:
            pin.high()

    def display_number(self, number):
        converted_num = str(number)
        while len(converted_num) < 4:
            converted_num = " " + converted_num
        index = 0
        for char in converted_num:
            self.print_7_seg_number(index, char)
            time.sleep(0.005)
            index += 1
            
