include("$(PORT_DIR)/boards/manifest.py")
freeze("./modules")
require("sht3x")
freeze("../../../../../gc9a01_mpy/modules")
