# -*- coding: utf-8 -*-
#!/usr/bin/env python
# cython: language_level=3

# implemented by Hori

import cython
from lib cimport la_class

@cython.locals(x=cython.double, y=cython.double, xv=cython.double, yv=cython.double)
cdef bint isOurShoot( la_class.WorldModel wm, la_class.ServerParam sp, int cycle, str side )

@cython.locals(x=cython.double, y=cython.double, xv=cython.double, yv=cython.double)
cdef bint isOppShoot( la_class.WorldModel wm, la_class.ServerParam sp, int cycle, str side )
