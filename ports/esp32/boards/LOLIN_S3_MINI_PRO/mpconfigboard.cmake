set(IDF_TARGET esp32s3)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    boards/sdkconfig.usb
    boards/sdkconfig.ble
    boards/sdkconfig.240mhz
    boards/sdkconfig.spiram_sx
    boards/LOLIN_S3_MINI_PRO/sdkconfig.board
)

set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)

# set(USER_C_MODULES ${GC9A01_MPY_DIR}/gc9a01_mpy/src/micropython.cmake)

if (GC9A01_MPY_DIR)
    set(USER_C_MODULES ${GC9A01_MPY_DIR}/gc9a01_mpy/src/micropython.cmake)
else ()
    set(USER_C_MODULES ${MICROPY_DIR}/../gc9a01_mpy/src/micropython.cmake)
endif()



