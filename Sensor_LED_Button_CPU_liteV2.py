from gpiozero import Button, LED
import time
from signal import pause

led = LED(18)
button = Button(26)

button.when_pressed = led.on
button.when_released = led.off

pause()
