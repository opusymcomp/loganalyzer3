#!/usr/bin/env python
# cython: language_level=3

import cython

from lib import la_class


def getInitialPosition( line: str, wm: la_class.WorldModel ) -> None:

    if ( line.split()[0].split(",")[0] != "0" ):
        return

    if ( "(move" in line ):
        move_teamname: cython.str = line.split()[2].rsplit( "_", 1 )[0]
        # move_cycle: cython.int = int( line.split()[0].split( "," )[0] )
        move_player: cython.int = int( line.split()[2].rsplit( "_", 1 )[1].strip( ":" ) )

        for i in range( len( line.split() ) ):
            if ( "move" in line.split()[i] ):
                seq = i

        if ( wm.l.name == move_teamname ):
            wm.l.player[ move_player - 1 ].pos.x = float( line.split()[seq+1] )
            try:
                wm.l.player[ move_player - 1 ].pos.y = float( line.split()[seq+2].split(")(")[0] )
            except ValueError:
                wm.l.player[ move_player - 1 ].pos.y = float( line.split()[seq+2].replace(")","") )
        elif ( wm.r.name == move_teamname ):
            wm.r.player[ move_player - 1 ].pos.x = float( line.split()[seq+1] )
            try:
                wm.r.player[ move_player - 1 ].pos.y = float( line.split()[seq+2].split(")(")[0] )
            except ValueError:
                wm.r.player[ move_player - 1 ].pos.y = float( line.split()[seq+2].replace(")","") )


def getAction( line: str, wm: la_class.WorldModel ) -> None:

    teamname: cython.str = line.split()[2].rsplit( "_", 1 )[0]
    unum: cython.int = int( line.split()[2].rsplit( "_", 1 )[1].strip( ":" ) )

    if ( teamname == wm.l.name ):
        wm.l.player[unum - 1].action = line.split(": ")[1].strip( "\n" )
    elif ( teamname == wm.r.name ):
        wm.r.player[unum - 1].action = line.split(": ")[1].strip( "\n" )
