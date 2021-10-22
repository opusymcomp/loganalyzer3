#!/usr/bin/env python
# cython: language_level=3

import cython

from extraction import get_dash as gd
from lib import la_class

def countDribble( wm: list, cycle: cython.int, feat: la_class.Feature ) -> None:
    if ( wm[cycle + 1].last_kicker_unum == wm[cycle].last_kicker_unum ):
        if ( wm[cycle].dominate_side == feat.target_team ):
            if ( gd.isDash( wm, cycle ) ):
                if ( not __debug__ ):
                    print ("our_dribble",wm[cycle].last_kicker_unum + 1, \
                               "cycle", wm[cycle+1].last_kicked_cycle )
                feat.our_dribble += 1
        else:
            if ( gd.isDash( wm, cycle ) ):
                if ( not __debug__ ):
                    print ("opp_dribble",wm[cycle].last_kicker_unum + 1, \
                               "cycle", wm[cycle+1].last_kicked_cycle )
                feat.opp_dribble += 1
