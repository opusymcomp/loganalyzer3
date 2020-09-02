# -*- coding: utf-8 -*-
import os
import glob
import shutil

from distutils.core import setup, Extension
from Cython.Build import cythonize

compile_list = [
    #[library name, place of this library]
    ["la_class", "lib"],
    ["lib_log_analyzer", "lib"],
    ["option", "lib"],
    ["filename_split", "extraction"],
    ["get_tackle", "extraction"],
    ["get_kick", "extraction"],
    ["rcg_reader", "extraction"],
    ["rcl_reader", "extraction"],
    ["hetero", "extraction"],
    ["referee", "extraction"],
    ["extract", "extraction"],
    ["dribble_count", "calculation"],
    ["kick_distribution", "calculation"],
    ["kick_sequence", "calculation"],
    ["offside_line", "calculation"],
    ["pass_check", "calculation"],
    ["shoot", "calculation"],
    ["through_pass", "calculation"],
    ["calculate", "calculation"]
]

# compile
print("compile cython")
ext = []
for l_name, place in compile_list:
    ext.append(Extension(l_name, [place+"/"+l_name+".py"], include_dirs=["."]))
setup(name="loganalyzer3", ext_modules=cythonize(ext))

print("move libraries (some errors would be caused for Windows)")
# mv libraries
for l_name, place in compile_list:
    pathname = glob.glob("./"+l_name+".cpython-*-linux-gnu.so")[0]
    filename = os.path.split(pathname)[1]
    shutil.move(pathname, "./"+place+"/"+filename)

print("finish compilation!")
