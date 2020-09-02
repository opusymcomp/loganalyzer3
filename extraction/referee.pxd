#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

# --- format --- #
# goal [ cycle, team( l or r ) ]

@cython.locals(our_yellow_card=cython.int, tmp=cython.list)
cdef int countOurYellowCard( la_class.WorldModel wm, str team )

@cython.locals(opp_yellow_card=cython.int, tmp=cython.list)
cdef int countOppYellowCard( la_class.WorldModel wm, str team )

cdef str getCurrentPlayMode( str line )

cdef void setPlayMode( str current_play_mode, la_class.WorldModel wm )

cdef void sayMessage( str line,  la_class.WorldModel wm ):
