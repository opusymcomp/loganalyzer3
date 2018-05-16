from lib import state

def calcOffsideLine( args, wm ):

    off_l = 0
    off_r = 0

    for cycle in range( args.start_cycle, args.end_cycle+1 ):
        for unum in range( 11 ):
            if ( off_l > wm[ cycle - args.start_cycle ].l.player[unum].pos.x ):
                side = "l"
                if ( not state.isGoalie( cycle - args.start_cycle, unum, side, wm ) ):
                    off_l = wm[cycle - args.start_cycle].l.player[unum].pos.x

            if ( off_r < wm[ cycle - args.start_cycle ].r.player[unum].pos.x ):
                side = "r"
                if ( not state.isGoalie( cycle - args.start_cycle, unum, side, wm ) ):
                    off_r = wm[cycle - args.start_cycle].r.player[unum].pos.x

        wm[cycle - args.start_cycle].l.offsideLineX = off_l
        wm[cycle - args.start_cycle].r.offsideLineX = off_r

        off_l = 0
        off_r = 0
