#!/usr/bin/env python
# cython: language_level=3
# -*- coding: utf-8 -*

import cython

from lib import la_class

def isThroughPass( wm: list, cycle: cython.int ) -> cython.bint:
    last_kicked_cycle: cython.int = wm[cycle].last_kicked_cycle

    if ( wm[cycle+1].dominate_side == wm[cycle].dominate_side \
         and wm[cycle+1].last_kicker_unum != wm[cycle].last_kicker_unum ):

        if ( wm[cycle+1].dominate_side == "l" \
             and wm[cycle+1].ball.pos.x - wm[last_kicked_cycle].ball.pos.x > 5.0 \
             and wm[cycle+1].ball.pos.x > 15.0 \
             and wm[last_kicked_cycle].r.offsideLineX < wm[cycle+1].ball.pos.x ):

            return True

        if ( wm[cycle+1].dominate_side == "r" \
             and wm[cycle+1].ball.pos.x - wm[last_kicked_cycle].ball.pos.x < -5.0 \
             and wm[cycle+1].ball.pos.x < -15.0 \
             and wm[last_kicked_cycle].l.offsideLineX > wm[cycle+1].ball.pos.x ):

            return True

    return False


def countThroughPass( wm: list, cycle: cython.int, feat: la_class.Feature ) -> None:

    if ( isThroughPass( wm, cycle ) ):
        if ( not __debug__ ):
            print ( "this pass is through pass" )
        if ( wm[cycle+1].dominate_side == feat.target_team ):
            feat.our_through_pass += 1
        else:
            feat.opp_through_pass += 1
