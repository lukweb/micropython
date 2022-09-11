#!/usr/bin/env python3


import argparse
import glob
import itertools
import os
import re
import subprocess

def get_version_from_git():
    git_tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        ).strip()
    git_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        ).strip()

    return git_tag+"-"+git_hash


def main():
    dirs=glob.glob("./ports/esp32/build-*")    
    print(dirs)
    git_ver=get_version_from_git()
    print(git_ver)
    for d in dirs:
        name=d[d.find("build-")+6:]
        # print(name)
        try:
            os.rename(d+"/firmware.bin",d+"/firmware-"+name+"-"+git_ver+".bin")
        except:
            pass

if __name__ == "__main__":
    main()
