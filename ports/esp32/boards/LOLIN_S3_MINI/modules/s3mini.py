# LOLIN S3 MINI MicroPython Helper Library

from micropython import const
from machine import Pin
import neopixel

# Pin Assignments

# SPI
SPI_MOSI = const(11)
SPI_MISO = const(13)
SPI_CLK = const(12)

# I2C
I2C_SDA = const(35)
I2C_SCL = const(36)

# RGB_LED
RGB_DATA = const(47)
_rgb_led = neopixel.NeoPixel(Pin(RGB_DATA), 1)


def rgb_led(r=0, g=0, b=0):
    _rgb_led[0] = (g, r, b)
    _rgb_led.write()


# BUTTON
BUTTON = const(0)
button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)
