#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class


cdef bint checkTackle( str state )

@cython.locals(all_tackle=cython.int)
cdef int countOurTackle( la_class.WorldModel wm, str team )

@cython.locals(all_tackle=cython.int)
cdef int countOppTackle( la_class.WorldModel wm, str team ):

@cython.locals(success_tackle=cython.int)
cdef int countOurSuccessTackle( la_class.WorldModel wm, la_class.WorldModel next_wm, str team ):

@cython.locals(success_tackle=cython.int)
cdef int countOppSuccessTackle( la_class.WorldModel wm, la_class.WorldModel next_wm, str team ):
