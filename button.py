# from gpiozero import LED, Button
# from signal import pause

# led = LED(17)
# button = Button(2)

# button.when_pressed = led.on
# button.when_released = led.off

# pause()


from subprocess import call
from gpiozero import LED, Button
from signal import pause


button = Button(2)

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing

pause()
