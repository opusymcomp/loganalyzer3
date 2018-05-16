from . import rcg_reader as rcg
from . import rcl_reader as rcl
from . import hetero
from . import referee

from . import get_kick
from . import get_tackle

from lib import lib_log_analyzer as lib

def extractRcg( args, wm, sp ):

    cycle = 0
    current_play_mode = "unknown"

    for line in open( lib.getFileName( args.filename ) + ".rcg", "r" ):

        if ( "(player_type (id" in line ):
            hetero_id = int( line.split()[2].strip(")(player_speed_max") )
            hetero.getHetero( line, hetero_id, sp )


        if ( "(playmode" in line ):
            current_play_mode = referee.getCurrentPlayMode( line )


        if ( "(show" in line ):
            tmp_line = line.split()

            # consider analyze cycles
            if ( args.start_cycle > int( tmp_line[1] ) ):
                continue
            elif ( args.end_cycle < int( tmp_line[1] ) ):
                break


            if ( not lib.isSameCycle( int( tmp_line[1] ), cycle ) ):

                cycle = int( tmp_line[1] )

                rcg.getInformation( tmp_line, wm[ cycle - args.start_cycle ] )
                referee.setPlayMode( current_play_mode, wm[ cycle - args.start_cycle ] )

                if ( cycle == 2999 ):
                    rcg.getInformation( tmp_line, wm[ cycle + 1 - args.start_cycle ] )
                    wm[cycle+1].referee.playmode = "time_over"


def extractRcl( args, wm, sp ):

    cycle = 0

    for line in open( lib.getFileName( args.filename ) + ".rcl", "r" ):

        # consider analyze cycles
        if ( args.start_cycle > int( line.split()[0].split( "," )[0] ) ):
            continue
        elif ( args.end_cycle < int( line.split()[0].split( "," )[0] ) ):
            break

        # initial position
        rcl.getInitialPosition( line, wm[0] )

        # getActions( Only playon )
        if ( lib.isSameCycle( int( line.split()[0].split( "," )[1] ), 0 ) ):

            # ignore coach and referee
            if ( not "_Coach" in line \
                 and not "(referee" in line ):
                cycle = int( line.split()[0].split( "," )[0] )
                rcl.getAction( line, wm[ cycle - args.start_cycle ] )

        if ( "(referee" in line ):
            cycle = int( line.split()[0].split( "," )[0] )
            referee.sayMessage( line, wm[ cycle - args.start_cycle ] )
