# -*- coding: utf-8 -*-
#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(INVALID_VALUE=cython.double, START_SEQUENCE=cython.int, BETWEEN_SEQUENCE=cython.int, END_SEQUENCE=cython.int,
               POSITIVE_LABEL=cython.int, NEGATIVE_LABEL=cython.int, tmp_kick_path_x=cython.list, tmp_kick_path_y=cython.list,
               tmp_kick_sequence=cython.list)
cdef void appendSequence( la_class.Feature feat, str color, double kick_dist_thr=? )

# cdef printSequence( la_class.ServerParam sp, la_class.Feature feat ):

cdef void finishSequence( la_class.Feature feat, str color )

cdef void clearList( la_class.Feature feat )

@cython.locals(last_kick_side=cython.str, last_kick_cycle=cython.int, kick_side=cython.str, kick_cycle=cython.int,
               NO_KICK=cython.int, NO_KICKER=cython.int, NO_RECEIVER=cython.int, kicked_from=cython.int, kicked_to=cython.int,
               )
cdef int getSequence( la_class.WorldModel wm, la_class.ServerParam sp, int cycle, la_class.Feature feat, bint until_penalty_area=?)

cdef void considerSameTimingKick( la_class.WorldModel wm, int cycle, int start_cycle, la_class.Feature feat)

cdef void saveKickSequence( la_class.Feature feat, bint outputKickedCycle=?)