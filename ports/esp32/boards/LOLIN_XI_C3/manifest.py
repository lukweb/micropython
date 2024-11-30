include("$(PORT_DIR)/boards/manifest.py")
freeze("./modules")
require("sht3x")
freeze("../../../../../st7789_mpy/fonts/bitmap")