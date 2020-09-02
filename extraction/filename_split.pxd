#!/usr/bin/env python
# cython: language_level=3

import cython

@cython.locals(left=cython.str, right=cython.str, lpoint=cython.str, rpoint=cython.str, getpoint=cython.int, lostpoint=cython.int)
cdef list splitFileName( str filename, str logname, str team ):