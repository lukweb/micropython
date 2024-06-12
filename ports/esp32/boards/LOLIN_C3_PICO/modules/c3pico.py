# LOLIN C3 PICO MicroPython Helper Library

from micropython import const
from machine import Pin, ADC
import neopixel

# Pin Assignments

# SPI
SPI_MOSI = const(4)
SPI_MISO = const(0)
SPI_CLK = const(1)

# I2C
I2C_SDA = const(8)
I2C_SCL = const(10)

# RGB_LED
RGB_DATA = const(7)
_rgb_led = neopixel.NeoPixel(Pin(RGB_DATA), 1)

# BUTTON
BUTTON = const(9)

# Battery ADC Pin
BATTERY_ADC = const(3)

# Built-in peripherals

button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)


def rgb_led(r=0, g=0, b=0):
    _rgb_led[0] = (g, r, b)
    _rgb_led.write()


def get_battery_voltage():
    adc_battery = ADC(Pin(BATTERY_ADC), atten=ADC.ATTN_11DB)
    val = adc_battery.read_uv() * 2 / 1000000
    return val
