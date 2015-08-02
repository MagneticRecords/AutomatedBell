# AutomatedBell
Rings every time an angel gets his wings (or First Opinion account).

## How it works

Basically, the circuit we build triggers the solenoids to rapidly move the nail down onto the xylophone, then get pulled back up by the rubber band.

## The Code

Each of the solenoids is hooked up to its indiviual pin on the Raspberry Pi. These pins are controlled by the Pi's own build-in GPIO/RPi api. The pins are initialized by this code:

```
pins = [12,16,18,22,32,36,38,40] #the numbers are the id's of the pins that were available for GPIO output (some are reserved for grounding, etc.)
GPIO.setmode(GPIO.BOARD)
for x in pins:
   GPIO.setup(x,GPIO.OUT)
```

Then the pin is triggered by the following command:

```
GPIO.output(pins[pinid],GPIO.HIGH)  #turn pin on
GPIO.output(pins[pini],GPIO.LOW)    #turn pin off
```

The two commands are separated by about a 0.05 second interval.
