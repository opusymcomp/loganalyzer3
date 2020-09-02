#!/usr/bin/env python
# cython: language_level=3

from lib cimport la_class
cdef void countDribble( la_class.WorldModel wm, int cycle, la_class.Feature feat )