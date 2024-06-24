# LOLIN D32 Pro MicroPython Helper Library

from micropython import const
from machine import Pin


# Pin Assignments

# SPI
SPI_MOSI = const(23)
SPI_CLK = const(18)
SPI_MISO = const(19)

# I2C
I2C_SDA = const(21)
I2C_SCL = const(22)

# TFT
TFT_LED = const(32)
TFT_RST = const(33)
TFT_DC = const(27)
TFT_CS = const(14)

TS_CS = const(12)

# Micro SD
TF_CS = const(4)

# LED
LED = const(5)

# Helper methods for built in sensors

led = Pin(LED, Pin.OUT, value=1)
