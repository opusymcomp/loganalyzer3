#!/usr/bin/env python
# cython: language_level=3

import os
import cython

from lib cimport la_class

@cython.locals(cycle=cython.int, current_play_mode=cython.str, hetero_id=cython.int, tmp_line=cython.list, tmp_result=cython.list)
cdef void extractRcg( list args, la_class.WorldModel[:] wm, la_class.SeverParam sp, la_class.Feature feature)

@cython.locals(filename=cython.str, cycle=cython.int)
cdef void extractRcl(list args, la_class.WorldModel[:] wm, la_class.SeverParam sp)
