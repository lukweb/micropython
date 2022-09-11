#!/usr/bin/env python3


import argparse
import glob
import itertools
import os
import re
import subprocess




def main():
    dirs=glob.glob("./ports/esp32/build-*")    
    print(dirs)
    for d in dirs:
        name=d[d.find("build-")+6:]
        # print(name)
        try:
            os.rename(d+"/firmware.bin",d+"/firmware-"+name+".bin")
        except:
            pass

if __name__ == "__main__":
    main()
