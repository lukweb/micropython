#!/bin/bash

if which nproc > /dev/null; then
    MAKEOPTS="-j$(nproc)"
else
    MAKEOPTS="-j$(sysctl -n hw.ncpu)"
fi

########################################################################################
# general helper functions

function ci_gcc_arm_setup {
    sudo apt-get install gcc-arm-none-eabi libnewlib-arm-none-eabi
    arm-none-eabi-gcc --version
}

########################################################################################
# code formatting

function ci_code_formatting_setup {
    sudo apt-get install uncrustify
    pip3 install black
    uncrustify --version
    black --version
}

function ci_code_formatting_run {
    tools/codeformat.py -v
}

########################################################################################
# commit formatting

function ci_commit_formatting_run {
    git remote add upstream https://github.com/micropython/micropython.git
    git fetch --depth=100 upstream  master
    # For a PR, upstream/master..HEAD ends with a merge commit into master, exlude that one.
    tools/verifygitlog.py -v upstream/master..HEAD --no-merges
}

########################################################################################
# code size

function ci_code_size_setup {
    sudo apt-get update
    sudo apt-get install gcc-multilib
    gcc --version
    ci_gcc_arm_setup
}

function ci_code_size_build {
    # starts off at either the ref/pull/N/merge FETCH_HEAD, or the current branch HEAD
    git checkout -b pull_request # save the current location
    git remote add upstream https://github.com/micropython/micropython.git
    git fetch --depth=100 upstream master
    # build reference, save to size0
    # ignore any errors with this build, in case master is failing
    git checkout `git merge-base --fork-point upstream/master pull_request`
    git show -s
    tools/metrics.py clean bm
    tools/metrics.py build bm | tee ~/size0 || true
    # build PR/branch, save to size1
    git checkout pull_request
    git log upstream/master..HEAD
    tools/metrics.py clean bm
    tools/metrics.py build bm | tee ~/size1
}

########################################################################################
# .mpy file format

function ci_mpy_format_setup {
    sudo pip3 install pyelftools
}

function ci_mpy_format_test {
    # Test mpy-tool.py dump feature on bytecode
    python2 ./tools/mpy-tool.py -xd ports/minimal/frozentest.mpy
    python3 ./tools/mpy-tool.py -xd ports/minimal/frozentest.mpy

    # Test mpy-tool.py dump feature on native code
    make -C examples/natmod/features1
    ./tools/mpy-tool.py -xd examples/natmod/features1/features1.mpy
}


########################################################################################
# ports/esp32

function ci_esp32_setup_helper {
    pip3 install pyelftools
    git clone https://github.com/espressif/esp-idf.git
    git -C esp-idf checkout $1
    git -C esp-idf submodule update --init \
        components/bt/host/nimble/nimble \
        components/esp_wifi \
        components/esptool_py/esptool \
        components/lwip/lwip \
        components/mbedtls/mbedtls
    if [ -d esp-idf/components/bt/controller/esp32 ]; then
        git -C esp-idf submodule update --init \
            components/bt/controller/lib_esp32 \
            components/bt/controller/lib_esp32c3_family
    else
        git -C esp-idf submodule update --init \
            components/bt/controller/lib
    fi
    ./esp-idf/install.sh
}

function ci_esp32_idf402_setup {
    ci_esp32_setup_helper v4.0.2
}

function ci_esp32_idf44_setup {
    ci_esp32_setup_helper v4.4
}

function ci_esp32_build {
    source esp-idf/export.sh
    make ${MAKEOPTS} -C mpy-cross
    make ${MAKEOPTS} -C ports/esp32 submodules
    make ${MAKEOPTS} -C ports/esp32 \
        USER_C_MODULES=../../../examples/usercmodule/micropython.cmake \
        FROZEN_MANIFEST=$(pwd)/ports/esp32/boards/manifest_test.py
    if [ -d $IDF_PATH/components/esp32c3 ]; then
        make ${MAKEOPTS} -C ports/esp32 BOARD=GENERIC_C3
    fi
    if [ -d $IDF_PATH/components/esp32s2 ]; then
        make ${MAKEOPTS} -C ports/esp32 BOARD=GENERIC_S2
    fi
    if [ -d $IDF_PATH/components/esp32s3 ]; then
        make ${MAKEOPTS} -C ports/esp32 BOARD=GENERIC_S3
    fi

    # Test building native .mpy with xtensawin architecture.
    ci_native_mpy_modules_build xtensawin
}

function ci_esp32_lolin_build {
    source esp-idf/export.sh
    make ${MAKEOPTS} -C mpy-cross
    make ${MAKEOPTS} -C ports/esp32 submodules
    
    make ${MAKEOPTS} -C ports/esp32 BOARD=$1
    

}

function ci_lolin_c3_mini_build {
    ci_esp32_lolin_build LOLIN_C3_MINI
}

function ci_lolin_build {
    source esp-idf/export.sh
    make ${MAKEOPTS} -C mpy-cross
    make ${MAKEOPTS} -C ports/esp32 submodules
    
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_C3_MINI
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_S2_MINI
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_S2_PICO
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_S3
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_C3_PICO
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_D32
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_D32_PRO
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_S3_PRO
    # make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_S3_MINI
    make ${MAKEOPTS} -C ports/esp32 BOARD=LOLIN_S3_MINI_PRO

}


########################################################################################
# ports/esp8266

function ci_esp8266_setup {
    sudo pip install pyserial esptool==3.3.1
    wget https://github.com/jepler/esp-open-sdk/releases/download/2018-06-10/xtensa-lx106-elf-standalone.tar.gz
    zcat xtensa-lx106-elf-standalone.tar.gz | tar x
    # Remove this esptool.py so pip version is used instead
    rm xtensa-lx106-elf/bin/esptool.py
}

function ci_esp8266_path {
    echo $(pwd)/xtensa-lx106-elf/bin
}

function ci_esp8266_build {
    make ${MAKEOPTS} -C mpy-cross
    make ${MAKEOPTS} -C ports/esp8266 submodules
    make ${MAKEOPTS} -C ports/esp8266 BOARD=LOLIN_D1_MINI
}

function ci_gc9a01_mpy_setup {
    git clone https://github.com/wemos/gc9a01_mpy.git
    git -C gc9a01_mpy checkout master
    ls ./gc9a01_mpy
}
