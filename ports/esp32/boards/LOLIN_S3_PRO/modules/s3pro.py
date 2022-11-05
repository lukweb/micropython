# LOLIN S3 Pro MicroPython Helper Library

from micropython import const
from machine import Pin
import neopixel

# Pin Assignments

# SPI
SPI_MOSI = const(11)
SPI_MISO = const(13)
SPI_CLK = const(12)

# TF/MicroSD
TF_CS = const(46)

# Display(TFT)
TS_CS = const(45)
TFT_CS = const(48)
TFT_DC = const(47)
TFT_RST = const(21)
TFT_LED = const(14)

# I2C
I2C_SDA = const(9)
I2C_SCL = const(10)

# RGB_LED
RGB_DATA = const(38)
_rgb_led = neopixel.NeoPixel(Pin(RGB_DATA), 1)


def rgb_led(r=0, g=0, b=0):
    _rgb_led[0] = (g, r, b)
    _rgb_led.write()


# BUTTON
BUTTON = const(0)
button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)
