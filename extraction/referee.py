#!/usr/bin/env python
# cython: language_level=3

# goal [ cycle, team( l or r ) ]

import cython

from lib import la_class


def countOurYellowCard( wm: la_class.WorldModel, team: str ) -> cython.int:

    our_yellow_card: cython.int = 0

    for say in wm.referee.say:
        if ( "(referee yellow_card_" in say ):
            tmp: list = say.split( "_" )
            if ( tmp[2] == team ):
                our_yellow_card = 1

    return our_yellow_card


def countOppYellowCard( wm: la_class.WorldModel, team: str ) -> cython.int:

    opp_yellow_card: cython.int = 0

    for say in wm.referee.say:
        if ( "(referee yellow_card_" in say ):
            tmp: list = say.split( "_" )
            if ( tmp[2] != team ):
                opp_yellow_card = 1

    return opp_yellow_card


def getCurrentPlayMode( line: str ) -> str:

    return line.split()[2].strip( ")" )


def setPlayMode( current_play_mode: str, wm: la_class.WorldModel ) -> None:

        wm.referee.playmode = current_play_mode


def sayMessage( line: str, wm: la_class.WorldModel ) -> None:

    wm.referee.say.append( line )
