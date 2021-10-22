#!/usr/bin/env python
# cython: language_level=3

import cython

from lib import la_class


def isGoalie( cycle: cython.int, unum: cython.int, side: str, wm: list ) -> cython.bint:

    if ( side == "l" ):
        if( int( wm[cycle].l.player[unum].state, 16 ) & int( 0x00000008 ) == 8 ):
            return True
        else:
            return False

    elif ( side == "r"):
        if( int( wm[cycle].r.player[unum].state, 16 ) & int( 0x00000008 ) == 8 ):
            return True
        else:
            return False

def isDead( cycle: cython.int, unum: cython.int, side: str, wm: list ) -> cython.bint:

    if ( side == 'l' ):
        if ( wm[cycle].l.player[unum].state == '0' ):
            return True
        else:
            return False

    elif ( side == 'r' ):
        if ( wm[cycle].r.player[unum].state == '0' ):
            return True
        else:
            return False


def checkTackle( state: str ) -> cython.bint:
    if ( int( state, 16 ) & int( 0x00002000 ) == 8192 ):
        return False
    else:
        return True


def checkKick( wm: la_class.WorldModel, unum: cython.int, side: str ) -> cython.bint:

    if ( side == "l" ):
        if ( int( wm.l.player[unum].state, 16 ) & int( 0x00000004 ) == 4 ):
            return False

        else:
            return True

    elif ( side == "r" ):
        if ( int( wm.r.player[unum].state, 16 ) & int( 0x00000004 ) == 4 ):
            return False

        else:
            return True
