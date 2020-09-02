#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(direction=cython.double)
cdef str countKick( la_class.WorldModel wm, int cycle, la_class.Feature feat )

cdef void countPass( la_class.WorldModel wm, int cycle, str direction, la_class.Feature feat ):

@cython.locals(last_kicked_cycle=cython.int, radian=cython.double, degree=cython.double)
cdef str getPassRoute( la_class.WorldModel wm, int cycle ):
