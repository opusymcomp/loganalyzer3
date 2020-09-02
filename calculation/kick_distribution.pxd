# -*- coding: utf-8 -*-
#!/usr/bin/env python
# cython: language_level=3

import cython
from lib cimport la_class

@cython.locals(degree=cython.double)
cdef void saveKickDistribution( la_class.Feature feat )

# cdef printKickDistribution( la_class.ServerParam sp, la_class.Feature feat ):
