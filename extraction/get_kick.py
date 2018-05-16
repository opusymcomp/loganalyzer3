from lib import lib_log_analyzer as lib

from extraction import get_tackle as gt


def checkKick( wm, unum, side ):

    if ( side == "l" ):
        if ( int( wm.l.player[unum].state, 16 ) & int( 0x00000004 ) == 4 ):
            return False

        else:
            return True

    elif ( side == "r" ):
        if ( int( wm.r.player[unum].state, 16 ) & int( 0x00000004 ) == 4 ):
            return False

        else:
            return True


def isKick( wm, cycle ):

    num_kick = 0
    kick_side_l = False
    kick_side_r = False

    for unum in range( 11 ):

        if ( ( "(kick" in wm[cycle].l.player[unum].action \
               or "(tackle" in wm[cycle].l.player[unum].action ) \
             and ( checkKick( wm[cycle+1], unum, "l" ) \
                   and gt.checkTackle( wm[cycle+1].l.player[unum].state ) )
             and not wm[cycle].referee.said ):

            num_kick += 1
            wm[ cycle + 1 ].last_kicker_unum = unum
            wm[ cycle + 1 ].last_kicked_cycle = cycle + 1
            kick_side_l = True


        if ( ( "(kick" in wm[cycle].r.player[unum].action \
               or "(tackle" in wm[cycle].r.player[unum].action ) \
             and ( checkKick( wm[cycle+1], unum, "r" ) \
                   and gt.checkTackle( wm[cycle+1].r.player[unum].state ) )
             and not wm[cycle].referee.said ):

            num_kick += 1
            wm[ cycle + 1 ].last_kicker_unum = unum
            wm[ cycle + 1 ].last_kicked_cycle = cycle + 1
            kick_side_r = True


    if ( kick_side_l and kick_side_r ):
        wm[ cycle + 1 ].dominate_side = "neutral"
        wm[ cycle + 1 ].last_kicker_unum = -1
        return num_kick

    elif ( kick_side_l ):
        wm[ cycle + 1 ].dominate_side = "l"
        return num_kick

    elif ( kick_side_r ):
        wm[ cycle + 1 ].dominate_side = "r"
        return num_kick

    wm[ cycle + 1 ].dominate_side = wm[ cycle ].dominate_side
    wm[ cycle + 1 ].last_kicker_unum = wm[ cycle ].last_kicker_unum
    wm[ cycle + 1 ].last_kicked_cycle = wm[ cycle ].last_kicked_cycle
    return num_kick
