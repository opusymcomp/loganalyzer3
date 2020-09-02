#!/usr/bin/env python
# cython: language_level=3

from lib cimport la_class


cdef void getInformation( str[:] tmp_line, la_class.WorldModel wm )

cdef void getBallInformation( str[:] tmp_line, la_class.WorldModel wm )

cdef void getLeftTeamInformation( str[:] tmp_line, la_class.WorldModel wm )

cdef void getRightTeamInformation( str[:] tmp_line, la_class.WorldModel wm )