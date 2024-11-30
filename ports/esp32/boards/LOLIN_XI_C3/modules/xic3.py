# LOLIN XI C3 MicroPython Helper Library

from micropython import const
from machine import Pin

# Pin Assignments

# SPI
SPI_MOSI = const(4)
SPI_MISO = None
SPI_CLK = const(5)

# I2C
I2C_SDA = const(0)
I2C_SCL = const(3)

# TFT
TFT_RST = const(2)
TFT_DC = const(10)
TFT_MOSI = const(4)
TFT_SCK = const(5)
TFT_BL = const(1)

# EC11
EC11_OUT_A = const(7)
EC11_OUT_B = const(6)
EC11_OUT_E = const(8)

# BUTTON
BUTTON = const(9)

# Built-in peripherals

ec11_a=Pin(EC11_OUT_A,Pin.IN, Pin.PULL_UP)
ec11_b=Pin(EC11_OUT_B,Pin.IN, Pin.PULL_UP)
ec11_e=Pin(EC11_OUT_E, Pin.IN, Pin.PULL_UP)

button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

backlight=Pin(TFT_BL, Pin.OUT, value=0)
