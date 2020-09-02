#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

cdef bint checkKick( la_class.WorldModel wm, int unum, str side ):

@cython.locals(num_kick=cython.int, kick_side_l=cython.bint, kick_side_r=cython.bint)
cdef int isKick( la_class.WorldModel wm, int cycle )
