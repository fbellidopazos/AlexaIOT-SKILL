from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


rem_pi = PiGPIOFactory(host="192.168.1.62")

led = LED(18, pin_factory=rem_pi)
led.on()
