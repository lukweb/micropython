#define MICROPY_HW_BOARD_NAME "LOLIN D1 MINI"
#define MICROPY_HW_MCU_NAME "ESP8266"

#define MICROPY_PERSISTENT_CODE_LOAD    (1)
#define MICROPY_EMIT_XTENSA             (1)
#define MICROPY_EMIT_INLINE_XTENSA      (1)

#define MICROPY_DEBUG_PRINTERS          (1)
#define MICROPY_ERROR_REPORTING         (MICROPY_ERROR_REPORTING_NORMAL)

#define MICROPY_READER_VFS              (MICROPY_VFS)
#define MICROPY_VFS                     (1)

#define MICROPY_PY_UCRYPTOLIB           (1)

#define MICROPY_HW_I2C0_SCL                 (5)
#define MICROPY_HW_I2C0_SDA                 (4)

#define MICROPY_HW_SPI1_MOSI                (13)
#define MICROPY_HW_SPI1_MISO                (12)
#define MICROPY_HW_SPI1_SCK                 (14)
