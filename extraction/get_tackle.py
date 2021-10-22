#!/usr/bin/env python
# cython: language_level=3

import cython

from lib import la_class

def checkTackle( state: str ) -> cython.bint:
    if ( int( state, 16 ) & int( 0x00002000 ) == 8192 ):
        return False
    else:
        return True


def countOurTackle( wm: la_class.WorldModel, team: str ) -> cython.int:
    all_tackle: cython.int = 0

    if ( team  == "l" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.l.player[unum].action ):
                all_tackle += 1

    elif ( team == "r" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.r.player[unum].action ):
                all_tackle += 1

    return all_tackle


def countOppTackle( wm: la_class.WorldModel, team: str ) -> cython.int:
    all_tackle: cython.int = 0

    if ( team  == "l" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.r.player[unum].action ):
                all_tackle += 1

    elif ( team == "r" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.l.player[unum].action ):
                all_tackle += 1

    return all_tackle


def countOurSuccessTackle( wm: la_class.WorldModel, next_wm: la_class.WorldModel, team: str ) -> cython.int:
    success_tackle: cython.int = 0

    if ( team == "l" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.l.player[unum].action \
                 and checkTackle( next_wm.l.player[unum].state ) ):
                success_tackle += 1

    if ( team == "r" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.r.player[unum].action \
                 and checkTackle( next_wm.r.player[unum].state ) ):
                success_tackle += 1

    return success_tackle


def countOppSuccessTackle( wm: la_class.WorldModel, next_wm: la_class.WorldModel, team: str ) -> cython.int:
    success_tackle: cython.int = 0

    if ( team == "l" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.r.player[unum].action \
                 and checkTackle( next_wm.r.player[unum].state ) ):
                success_tackle += 1

    if ( team == "r" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.l.player[unum].action \
                 and checkTackle( next_wm.l.player[unum].state ) ):
                success_tackle += 1

    return success_tackle
