from machine import Pin
import time


def clear_segment_pins():
    for pin in range(4, 11):
        Pin(pin, Pin.OUT).value(0)


class FourDigitSevenSegment:
    # Pin to segment map
    __A = Pin(4, Pin.OUT)
    __B = Pin(5, Pin.OUT)
    __C = Pin(6, Pin.OUT)
    __D = Pin(7, Pin.OUT)
    __E = Pin(8, Pin.OUT)
    __F = Pin(9, Pin.OUT)
    __G = Pin(10, Pin.OUT)

    __num = {' ': (),
             '0': (__A, __B, __C, __D, __E, __F),
             '1': (__B, __C),
             '2': (__A, __B, __G, __E, __D),
             '3': (__A, __B, __G, __C, __D),
             '4': (__F, __G, __B, __C),
             '5': (__A, __F, __G, __C, __D),
             '6': (__A, __F, __E, __D, __C, __G),
             '7': (__A, __B, __C, __F),
             '8': (__A, __B, __C, __D, __E, __F, __G),
             '9': (__F, __A, __B, __G, __C, __D)}

    def print_7_seg_number(self, index, digit):
        clear_segment_pins()
        for pin in range(0, 4):
            if pin != index:
                Pin(pin, Pin.OUT).value(1)
            else:
                Pin(pin, Pin.OUT).value(0)

        Pin(index, Pin.OUT).value(0)
        for pin in self.__num[digit]:
            pin.value(1)
        time.sleep(0.001)


    def display_number(self, number):
        converted_num = str(number)
        while len(converted_num) < 4:
            converted_num = " " + converted_num
        index = 0
        for char in converted_num:
            self.print_7_seg_number(index, char)
            index += 1
