from extraction import get_kick as gk
from extraction import get_dash as gd
from lib import lib_log_analyzer as lib


def countDribble( wm, cycle, side, feat ):


    if ( wm[cycle + 1].last_kicker_unum == wm[cycle].last_kicker_unum ):

        if ( wm[cycle].dominate_side == side ):

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
