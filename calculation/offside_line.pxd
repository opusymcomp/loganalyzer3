#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(off_l=cython.int, off_r=cython.int, side=cython.str)
cdef void calcOffsideLine( list args, la_class.WorldModel wm )