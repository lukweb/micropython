# LOLIN D32 MicroPython Helper Library

from micropython import const
from machine import Pin


# Pin Assignments

# LED
LED = const(5)

# Helper methods for built in sensors

led = Pin(LED, Pin.OUT, value=1)
