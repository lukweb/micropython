"""LOLIN_XI_C3
"""

from machine import Pin, SPI
import st7789

TFA = 0
BFA = 0
WIDE = 0
TALL = 0

def config(rotation=1, buffer_size=0, options=0):

    spi = SPI(1, baudrate=40000000,polarity=1,phase=1,sck=Pin(5), mosi=Pin(4))
    return st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(2, Pin.OUT),
        dc=Pin(10, Pin.OUT),
        inversion=True,
        rotation=rotation,
        options=options,
        buffer_size=buffer_size
    )
