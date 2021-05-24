# To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

# Getting started with CPX and CircuitPython intro on:
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

# Find example code for CPX on:
# https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples


# import CPX library
from adafruit_circuitplayground import cp
import time


while True:

    if cp.temperature > 30:
        for i in range(10):
            cp.pixels[i] = (255, 0, 0)
            cp.pixels.show()

    else:
        for i in range(10):
            cp.pixels[i] = (0, 0, 255)
            cp.pixels.show()

    time.sleep(0.25)
