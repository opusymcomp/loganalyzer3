# goal [ cycle, team( l or r ) ]

from lib import lib_log_analyzer as lib


def countOurYellowCard( wm, team ):

    our_yellow_card = 0

    for say in wm.referee.say:
        if ( "(referee yellow_card_" in say ):
            tmp = say.split( "_" )
            if ( tmp[2] == team ):
                our_yellow_card = 1

    return our_yellow_card


def countOppYellowCard( wm, team ):

    opp_yellow_card = 0

    for say in wm.referee.say:
        if ( "(referee yellow_card_" in say ):
            tmp = say.split( "_" )
            if ( tmp[2] != team ):
                opp_yellow_card = 1

    return opp_yellow_card



def getCurrentPlayMode( line ):

    return line.split()[2].strip( ")" )



def setPlayMode( current_play_mode, wm ):

        wm.referee.playmode = current_play_mode



def sayMessage( line, wm ):

    wm.referee.say.append( line )
