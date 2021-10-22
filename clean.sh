#!/bin/bash

# clean binaries created by cython
DIR=`dirname $0`

find ${DIR} -type f -name *cpython-*-linux-gnu.so -print0 | xargs -0 rm -rf
find ${DIR} -type f -name *.c -print0 | xargs -0 rm -rf
rm -r ./build/
