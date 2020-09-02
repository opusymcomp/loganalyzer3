#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(last_kicked_cycle=cython.int)
cdef bint isThroughPass( la_class.WorldModel wm, int cycle )

cdef void countThroughPass( la_class.WorldModel wm, int cycle, la_class.Feature feat )
