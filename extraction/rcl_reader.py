from lib import lib_log_analyzer as lib


def getInitialPosition( line, wm ):

    if ( line.split()[0].split(",")[0] != "0" ):
        return

    if ( "(move" in line ):
        move_teamname = line.split()[2].rsplit( "_", 1 )[0]
        move_cycle = int( line.split()[0].split( "," )[0] )
        move_player = int( line.split()[2].rsplit( "_", 1 )[1].strip( ":" ) )

        for i in range( len( line.split() ) ):
            if ( "move" in line.split()[i] ):
                seq = i

        if ( wm.l.name == move_teamname ):
            wm.l.player[ move_player - 1 ].pos.x = float( line.split()[seq+1] )
            wm.l.player[ move_player - 1 ].pos.y = float( line.split()[seq+2].split(")(")[0] )
        elif ( wm.r.name == move_teamname ):
            wm.r.player[ move_player - 1 ].pos.x = float( line.split()[seq+1] )
            wm.r.player[ move_player - 1 ].pos.y = float( line.split()[seq+2].split(")(")[0] )


def getAction( line, wm ):

    teamname = line.split()[2].rsplit( "_", 1 )[0]
    unum = int( line.split()[2].rsplit( "_", 1 )[1].strip( ":" ) )

    if ( teamname == wm.l.name ):
        wm.l.player[unum - 1].action = line.split(": ")[1].strip( "\n" )
    elif ( teamname == wm.r.name ):
        wm.r.player[unum - 1].action = line.split(": ")[1].strip( "\n" )
