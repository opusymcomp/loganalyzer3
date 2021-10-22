#!/usr/bin/env python
# cython: language_level=3

import cython


def isDash( wm: list, cycle: cython.int ) -> cython.bint:
    for unum in range( 11 ):
        if ( wm[cycle + 1].last_kicker_unum == wm[cycle].last_kicker_unum ):
            if cycle in range(wm[cycle].last_kicked_cycle , wm[cycle+1].last_kicked_cycle ):
                if ( "(dash" in wm[cycle].l.player[unum].action and wm[cycle+1].last_kicker_unum == unum ):
                    return True
                elif ( "(dash" in wm[cycle].r.player[unum].action and wm[cycle+1].last_kicker_unum == unum ):
                    return True
    return False