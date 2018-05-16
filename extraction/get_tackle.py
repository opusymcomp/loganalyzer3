from lib import lib_log_analyzer as lib


def checkTackle( state ):
    if ( int( state, 16 ) & int( 0x00002000 ) == 8192 ):
        return False
    else:
        return True


def countOurTackle( wm, team ):

    all_tackle = 0

    if ( team  == "l" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.l.player[unum].action ):
                all_tackle += 1

    elif ( team == "r" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.r.player[unum].action ):
                all_tackle += 1

    return all_tackle


def countOppTackle( wm, team ):

    all_tackle = 0

    if ( team  == "l" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.r.player[unum].action ):
                all_tackle += 1

    elif ( team == "r" ):
        for unum in range( 11 ):
            if ( "(tackle" in wm.l.player[unum].action ):
                all_tackle += 1

    return all_tackle


def countOurSuccessTackle( wm, next_wm, team ):

    success_tackle = 0

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




def countOppSuccessTackle( wm, next_wm, team ):

    success_tackle = 0

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
