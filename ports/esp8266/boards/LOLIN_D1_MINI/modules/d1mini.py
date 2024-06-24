# LOLIN D1 MINI MicroPython Helper Library

from micropython import const
from machine import Pin


# Pin Assignments

# SPI
SPI_MOSI = const(13)
SPI_CLK = const(14)
SPI_MISO = const(12)

# I2C
I2C_SDA = const(4)
I2C_SCL = const(5)

# LED
LED = const(2)

# Helper methods for built in sensors

led = Pin(LED, Pin.OUT, value=1)
