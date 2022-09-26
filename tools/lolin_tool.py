#!/usr/bin/env python3


import argparse
import glob
from hashlib import new
import itertools
import os
import re
import subprocess


def get_version_from_git():
    git_tag = subprocess.check_output(
        ["git", "describe"],
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    ).strip()

    return git_tag


def main():
    dirs = glob.glob("./ports/*/build-*")
    print(dirs)
    git_ver = get_version_from_git()
    print(git_ver)
    for d in dirs:
        name = d[d.find("build-") + 6 :]
        # print(name)
        try:

            new_name = d + "/firmware-" + name + "-" + git_ver + ".bin"

            if len(glob.glob(d + "/firmware.bin")) == 1:
                old_name = d + "/firmware.bin"  # for esp32
            elif len(glob.glob(d + "/firmware-combined.bin")) == 1:
                old_name = d + "/firmware-combined.bin"  # for esp8266
            else:
                old_name = ""

            if old_name != "":
                os.rename(old_name, new_name)
                print(old_name, " ---> ", new_name)

        except:
            pass


if __name__ == "__main__":
    main()
