#!/usr/bin/env python

from . import offside_line as ol

from . import pass_check as pc
from . import through_pass as tp
from . import shoot
from . import dribble_count as dc
from . import kick_sequence as ks

from extraction import referee
from extraction import get_tackle as gt
from extraction import get_kick as gk




def analyzeLog( args, wm, sp, feat, team ):

    # write index
    if ( not args.without_index ):
        feat.outputIndexForR( args.filename, team )

    ol.calcOffsideLine( args, wm )

    for cycle in range( args.start_cycle, args.end_cycle ):

        for say in wm[ cycle - args.start_cycle ].referee.say:
            if ( "offside" in say \
                 or "free_kick_" in say \
                 or "kick_in_" in say \
                 or "before_kick_off" in say \
                 or "kick_off" in say \
                 or "foul_charge_" in say \
                 or "goal_kick_" in say \
                 or "corner_kick_" in say \
                 or "drop_ball" in say ):
                wm[ cycle - args.start_cycle ].dominate_side = "neutral"
                wm[ cycle - args.start_cycle ].referee.said = True

            elif ( "goal_l" in say ):
                if ( not __debug__ ):
                    print ( "team l goal!" )
                if ( team == "l" ):
                    feat.our_point += 1
                elif ( team == "r" ):
                    feat.opp_point += 1

            elif ( "goal_r" in say ):
                if ( not __debug__ ):
                    print ( "team r goal!" )
                if ( team == "r" ):
                    feat.our_point += 1
                elif( team == "l" ):
                    feat.opp_point += 1

        if ( wm[ cycle - args.start_cycle ].dominate_side == "l"
             and wm[ cycle - args.start_cycle ].referee.playmode == "play_on" ):
            if ( team == "l" ):
                feat.our_dominate_time += 1
            if ( team == "r" ):
                feat.opp_dominate_time += 1

        if ( wm[ cycle - args.start_cycle ].dominate_side == "r"
             and wm[ cycle - args.start_cycle ].referee.playmode == "play_on" ):
            if ( team == "r" ):
                feat.our_dominate_time += 1
            if ( team == "l" ):
                feat.opp_dominate_time += 1

        feat.our_possession = feat.our_dominate_time / ( ( cycle + 1 ) - args.start_cycle )
        feat.opp_possession = feat.opp_dominate_time / ( ( cycle + 1 ) - args.start_cycle )

        feat.our_yellow += referee.countOurYellowCard( wm[ cycle - args.start_cycle ], team )
        feat.opp_yellow += referee.countOppYellowCard( wm[ cycle - args.start_cycle ], team )

        feat.all_our_tackle += gt.countOurTackle( wm[ cycle - args.start_cycle ], team )
        feat.all_opp_tackle += gt.countOppTackle( wm[ cycle - args.start_cycle ], team )
        feat.our_tackle += gt.countOurSuccessTackle( wm[ cycle - args.start_cycle ], wm[ cycle - args.start_cycle + 1 ], team )
        feat.opp_tackle += gt.countOppSuccessTackle( wm[ cycle - args.start_cycle ], wm[ cycle - args.start_cycle + 1 ], team )

        kick_count = gk.isKick( wm,  cycle - args.start_cycle  )

        # same timing kick( Intercept )
        if ( kick_count > 1 ):
            # finish kick sequence
            ks.finishSequence( feat, "ro-" )

            if ( not __debug__ ):
                if ( wm[ cycle - args.start_cycle ].dominate_side == "l" ):
                    print ("team r Intercept", cycle + 1 )
                elif ( wm[ cycle - args.start_cycle ].dominate_side == "r" ):
                    print ("team l Intercept", cycle + 1 )

        elif ( kick_count == 1 ):
            if ( shoot.isOurShoot( wm[ cycle - args.start_cycle + 1 ], sp, cycle, team ) ):
                feat.our_shoot += 1
            elif ( shoot.isOppShoot( wm[ cycle - args.start_cycle + 1 ], sp, cycle, team ) ):
                feat.opp_shoot += 1
            direction = pc.countKick( wm,  cycle - args.start_cycle , team, feat )
            pc.countPass( wm,  cycle - args.start_cycle , direction, team, feat )
            tp.countThroughPass( wm, cycle - args.start_cycle, team, feat )
            dc.countDribble( wm, cycle - args.start_cycle, team, feat )
            feat.our_penalty_area += ks.getSequence( wm, sp, cycle - args.start_cycle, team, feat )


        # output for each cycle
        if ( args.each_cycle ):
            if ( not args.without_index ):
                feat.outputIndexForIR( args.start_cycle+1, cycle+1 )
            feat.outputIntegrateResult( args.start_cycle+1, cycle+1 )

    feat.outputResult( args.filename, team )

    if ( not __debug__ ):
        ks.printSequence( sp )
