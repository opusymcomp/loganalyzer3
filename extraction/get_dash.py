from lib import lib_log_analyzer as lib

from extraction import get_kick as gk
from extraction import get_tackle as gt

def isDash( wm, cycle ):


    for unum in range( 11 ):

        if ( wm[cycle + 1].last_kicker_unum == wm[cycle].last_kicker_unum ):

            if cycle in range(wm[cycle].last_kicked_cycle , wm[cycle+1].last_kicked_cycle ):

                if ( "(dash" in wm[cycle].l.player[unum].action  \
                     and wm[cycle+1].last_kicker_unum == unum ):

                    return True

                elif ( "(dash" in wm[cycle].r.player[unum].action  \
                       and wm[cycle+1].last_kicker_unum == unum ):

                    return True
