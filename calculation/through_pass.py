#!/usr/bin/env python

def isThroughPass( wm, cycle ):

    last_kicked_cycle = wm[cycle].last_kicked_cycle

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




def countThroughPass( wm, cycle, team, feat ):

    if ( isThroughPass( wm, cycle ) ):
        if ( not __debug__ ):
            print ( "this pass is through pass" )
        if ( wm[cycle+1].dominate_side == team ):
            feat.our_through_pass += 1
        else:
            feat.opp_through_pass += 1
