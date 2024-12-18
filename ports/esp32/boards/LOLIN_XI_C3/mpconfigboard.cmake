set(IDF_TARGET esp32c3)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    boards/sdkconfig.ble
    boards/LOLIN_C3_MINI/sdkconfig.board
)

set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)

set(USER_C_MODULES ${MICROPY_BOARD_DIR}/../../../../../st7789_mpy/st7789/micropython.cmake)
