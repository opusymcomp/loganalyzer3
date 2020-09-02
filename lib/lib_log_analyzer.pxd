#!/usr/bin/env python
# cython: language_level=3

from lib cimport la_class

# index c


cdef double calcDist( la_class.Position pos1, la_class.Position pos2 )

cdef double calcDistC( double x1, double y1, double x2, double y2 )

cdef double calcRadian( la_class.Position pos1, la_class.Position pos2 )

cdef double calcRadianC( double x1, double y1, double x2, double y2 )

cdef double changeRadianToDegree(double radian)

cdef int countPlayOn( int cycle1, int cycle2, list situation )

# index g

cdef str getFileName( str data )

cdef int getResult( la_class.Feature feat )

cdef str getTeamName( str filename, str side )

# index i

cdef bint isPlayOn( int cycle, list situation )

cdef bint isSameCycle( int now_count, int pre_count )

# index s

cdef str selectTargetTeam( list args, str filename )

cdef list sortPlayerUnumFromPos( la_class.Position[:] player_list, la_class.Position target_pos )
