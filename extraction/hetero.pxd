#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(tmp=cython.list)
cdef void getHetero( str line, int h_id, la_class.ServerParam sp )