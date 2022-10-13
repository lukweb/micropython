include("$(PORT_DIR)/boards/manifest.py")
freeze("./modules")
require("sdcard")
require("sht3x")
