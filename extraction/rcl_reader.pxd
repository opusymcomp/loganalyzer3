#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(move_teamname=cython.str, move_cycle=cython.int, move_player=cython.int, seq=cython.int)
cdef void getInitialPosition( str line, la_class.WorldModel wm )

@cython.locals(teamname=cython.str, unum=cython.int)
cdef void getAction( str line, la_class.WorldModel wm )