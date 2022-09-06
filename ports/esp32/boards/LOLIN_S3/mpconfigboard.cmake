set(IDF_TARGET esp32s3)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    boards/sdkconfig.usb
<<<<<<< HEAD
=======
    boards/sdkconfig.ble
    boards/sdkconfig.240mhz
>>>>>>> lolin_s3
    boards/LOLIN_S3/sdkconfig.board
)

set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)