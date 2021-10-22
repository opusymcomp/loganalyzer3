#!/usr/bin/env python
# cython: language_level=3

import cython

from lib import la_class
from lib import lib_log_analyzer as lib


def countKick( wm: list, cycle: cython.int, feat: la_class.Feature ) -> str:

    # same timing kick is already considered
    if ( feat.target_team == "l" ):
        if ( wm[cycle+1].dominate_side == "l" ):

            direction: cython.str = getPassRoute( wm, cycle )

            if ( direction == "left" ):
                feat.our_kick[0] += 1
            elif ( direction == "right" ):
                feat.our_kick[1] += 1
            elif ( direction == "front" ):
                feat.our_kick[2] += 1
            elif ( direction == "back" ):
                feat.our_kick[3] += 1

        if ( wm[cycle+1].dominate_side == "r" ):

            direction: cython.str = getPassRoute( wm, cycle )

            if ( direction == "left" ):
                feat.opp_kick[0] += 1
            elif ( direction == "right" ):
                feat.opp_kick[1] += 1
            elif ( direction == "front" ):
                feat.opp_kick[2] += 1
            elif ( direction == "back" ):
                feat.opp_kick[3] += 1

    elif ( feat.target_team == "r" ):
        if ( wm[cycle+1].dominate_side == "l" ):

            direction: cython.str = getPassRoute( wm, cycle )

            if ( direction == "left" ):
                feat.opp_kick[0] += 1
            elif ( direction == "right" ):
                feat.opp_kick[1] += 1
            elif ( direction == "front" ):
                feat.opp_kick[2] += 1
            elif ( direction == "back" ):
                feat.opp_kick[3] += 1

        if ( wm[cycle+1].dominate_side == "r" ):

            direction: cython.str = getPassRoute( wm, cycle )

            if ( direction == "left" ):
                feat.our_kick[0] += 1
            elif ( direction == "right" ):
                feat.our_kick[1] += 1
            elif ( direction == "front" ):
                feat.our_kick[2] += 1
            elif ( direction == "back" ):
                feat.our_kick[3] += 1

    return direction


def countPass( wm: list, cycle: cython.int, direction: str, feat: la_class.Feature ) -> None:

    if ( wm[cycle+1].dominate_side == wm[cycle].dominate_side \
         and wm[cycle+1].last_kicker_unum != wm[cycle].last_kicker_unum ):

        if ( wm[cycle+1].dominate_side == feat.target_team ):

            if ( direction == "left" ):
                if ( not __debug__ ):
                    print ( "our", wm[cycle].last_kicker_unum+1, \
                            "left pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.our_pass[0] += 1
            elif ( direction == "right" ):
                if ( not __debug__ ):
                    print ( "our", wm[cycle].last_kicker_unum+1, \
                            "right pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.our_pass[1] += 1
            elif ( direction == "front" ):
                if ( not __debug__ ):
                    print ( "our", wm[cycle].last_kicker_unum+1, \
                            "front pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.our_pass[2] += 1
            elif ( direction == "back" ):
                if ( not __debug__ ):
                    print ( "our", wm[cycle].last_kicker_unum+1, \
                            "back pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.our_pass[3] += 1

        else:
            if ( direction == "left" ):
                if ( not __debug__ ):
                    print ( "opp", wm[cycle].last_kicker_unum+1, \
                            "left pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.opp_pass[0] += 1
            elif ( direction == "right" ):
                if ( not __debug__ ):
                    print ( "opp", wm[cycle].last_kicker_unum+1, \
                            "right pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.opp_pass[1] += 1
            elif ( direction == "front" ):
                if ( not __debug__ ):
                    print ( "opp", wm[cycle].last_kicker_unum+1, \
                            "front pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.opp_pass[2] += 1
            elif ( direction == "back" ):
                if ( not __debug__ ):
                    print ( "opp", wm[cycle].last_kicker_unum+1, \
                            "back pass:", wm[cycle].last_kicked_cycle, \
                            "to", wm[cycle+1].last_kicker_unum+1, \
                            "received:", wm[cycle+1].last_kicked_cycle )
                feat.opp_pass[3] += 1


def getPassRoute( wm: list, cycle:cython.int ) -> str:

    # check pass route. return -> left, right, front, back
    last_kicked_cycle: cython.int = wm[cycle].last_kicked_cycle
    radian: cython.double = lib.calcRadian( wm[ last_kicked_cycle ].ball.pos, wm[ cycle ].ball.pos )
    degree: cython.double = lib.changeRadianToDegree( radian )

    if( wm[cycle+1].dominate_side == "l" ):

        if( degree > -45.0 and degree <= 45.0 ):
            return "front"
        elif( degree > 45.0 and degree <= 135.0 ):
            return "right"
        elif( degree > 135.0 or degree <= -135.0 ):
            return "back"
        elif( degree > -135.0 and degree <= -45.0 ):
            return "left"

    elif ( wm[cycle+1].dominate_side == "r" ):

        if( degree > -45.0 and degree <= 45.0 ):
            return "back"
        elif( degree > 45.0 and degree <= 135.0 ):
            return "left"
        elif( degree > 135.0 or degree <= -135.0 ):
            return "front"
        elif( degree > -135.0 and degree <= -45.0 ):
            return "right"
