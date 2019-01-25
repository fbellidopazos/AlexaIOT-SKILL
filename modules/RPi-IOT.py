from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

#Raspberry GPIO
def on(pin_number,ip):
    rem_pi = PiGPIOFactory(host=str(ip))

    led = LED(pin_number, pin_factory=rem_pi)
    led.on()
    return
def off(pin_number,ip):
    rem_pi = PiGPIOFactory(host=str(ip))

    led = LED(pin_number, pin_factory=rem_pi)
    led.off()
    return
    
#Curtains Development
def cDown(pin_number,ip):
    rem_pi = PiGPIOFactory(host=str(ip))

    led = LED(pin_number, pin_factory=rem_pi)
    led.on()
    time.sleep( 5 )
    led.off()
    return
def cUp(pin_number,ip):
    rem_pi = PiGPIOFactory(host=str(ip))

    led = LED(pin_number, pin_factory=rem_pi)
    led.on()
    time.sleep( 5 )
    led.off()
    return
