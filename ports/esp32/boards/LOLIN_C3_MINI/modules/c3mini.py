# LOLIN C3 MINI MicroPython Helper Library

from micropython import const
from machine import Pin
import neopixel

# Pin Assignments

# SPI
SPI_MOSI = const(4)
SPI_MISO = const(0)
SPI_CLK = const(1)

# I2C
I2C_SDA = const(8)
I2C_SCL = const(10)

# LED
LED = const(7)

# RGB_LED
RGB_DATA = const(7)
_rgb_led = neopixel.NeoPixel(Pin(RGB_DATA), 1)

# BUTTON
BUTTON = const(9)

# Built-in peripherals

led = Pin(LED, Pin.OUT, value=0)
button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)


def rgb_led(r=0, g=0, b=0):
    _rgb_led[0] = (r, g, b)
    _rgb_led.write()
