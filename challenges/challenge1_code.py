# To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

# Getting started with CPX and CircuitPython intro on:
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

# Find example code for CPX on:
# https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples


# import CPX library
from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.8

RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)


def color_round(color):
    for i in range(10):
        cp.pixels[i] = color
        time.sleep(0.25)
        cp.pixels.show()
    time.sleep(0.25)


while True:
    color_round(RED)
    color_round(PURPLE)
    color_round(BLUE)
