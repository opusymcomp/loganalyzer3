#!/usr/bin/env python
# cython: language_level=3

from lib cimport la_class as la

cdef bint isGoalie( int cycle, int unum, str side, la.WorldModel[:] wm )

cdef bint isDead( int cycle, int unum, str side, la.WorldModel[:] wm )

cdef bint checkTackle( str state )

cdef bint checkKick( la.WorldModel[:]  wm, int unum, str side )