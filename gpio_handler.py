from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


class gpio_handler(object):
    def __init__(self, pin_number,ip):

        self.pin=int(pin_number)
        self.factory=PiGPIOFactory(host=str(ip))
        self.led=LED(int(pin_number), pin_factory=self.factory)

    def on(self):
        (self.led).on()
        print(str(self.pin)+" IS ON")
        return True

    def off(self):
        (self.led).off()
        print(str(self.pin)+" IS OFF")
        return True