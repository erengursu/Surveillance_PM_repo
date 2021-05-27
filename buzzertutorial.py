#Libraries
#https://peppe8o.com/use-passive-buzzer-with-raspberry-pi-and-python/
import RPi.GPIO as gpio
from time import sleep


class Buzzer(object):
    def __init__(self,pin_number):
        gpio.setmode(gpio.BOARD)
        self.pin_number=pin_number
        gpio.setup(pin_number, gpio.OUT, initial=gpio.HIGH)
        self.buzzer = gpio.PWM(self.pin_number, 1000) # Set frequency to 1 Khz
    def ringwarning(self):
        self.buzzer.start(40) # Set dutycycle to 10

    def ringerror(self):
        self.buzzer.start(70) # Set dutycycle to 50

    def stop(self):
        self.buzzer.stop()

    def __del__(self):
        gpio.cleanup(self.pin_number)

    def positiveresponse(self):
        for i in range(4):
            self.buzzer.start(50)
            sleep(0.5)
            self.buzzer.stop()
            sleep(0.2)

buzzer = Buzzer(33)
print("Positive response")
buzzer.positiveresponse()
print("Warning")
buzzer.ringwarning()
sleep(2)
buzzer.stop()
