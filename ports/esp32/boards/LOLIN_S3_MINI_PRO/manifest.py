include("$(PORT_DIR)/boards/manifest.py")
freeze("./modules")
require("sht3x")
require("qmi8658")
require("esp32_rmt_ir")
freeze("../../../../../gc9a01_mpy/modules")
