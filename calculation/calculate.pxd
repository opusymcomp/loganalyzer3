#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(kick_count=cython.int, direction=cython.str, l_disconnected_player=cython.int, r_disconnected_player=cython.int)
cdef void analyzeLog(list args, la_class.WorldModel[:] wm, la_class.ServerParam sp, la_class.Feature feat)