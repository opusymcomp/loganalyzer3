#!/usr/bin/env python

from . import offside_line as ol

from . import pass_check as pc
from . import through_pass as tp
from . import shoot
from . import dribble_count as dc
from . import kick_sequence as ks
from . import kick_distribution as kd

from extraction import referee
from extraction import get_tackle as gt
from extraction import get_kick as gk

from lib import state


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
                wm[ cycle - args.start_cycle ].dominate_side = "neutral"
                wm[ cycle - args.start_cycle ].referee.said = True
                if ( not __debug__ ):
                    print ( "team l goal!" )
                if ( team == "l" ):
                    feat.our_point += 1
                elif ( team == "r" ):
                    feat.opp_point += 1

            elif ( "goal_r" in say ):
                wm[ cycle - args.start_cycle ].dominate_side = "neutral"
                wm[ cycle - args.start_cycle ].referee.said = True
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

        feat.our_possession = float( feat.our_dominate_time / float( ( cycle + 1 ) - args.start_cycle ) )
        feat.opp_possession = float( feat.opp_dominate_time / float( ( cycle + 1 ) - args.start_cycle ) )

        feat.our_yellow += referee.countOurYellowCard( wm[ cycle - args.start_cycle ], team )
        feat.opp_yellow += referee.countOppYellowCard( wm[ cycle - args.start_cycle ], team )

        feat.all_our_tackle += gt.countOurTackle( wm[ cycle - args.start_cycle ], team )
        feat.all_opp_tackle += gt.countOppTackle( wm[ cycle - args.start_cycle ], team )
        feat.our_tackle += gt.countOurSuccessTackle( wm[ cycle - args.start_cycle ], wm[ cycle - args.start_cycle + 1 ], team )
        feat.opp_tackle += gt.countOppSuccessTackle( wm[ cycle - args.start_cycle ], wm[ cycle - args.start_cycle + 1 ], team )

        kick_count = gk.isKick( wm,  cycle - args.start_cycle )

        # same timing kick( Intercept )
        if ( kick_count > 1 and not wm[cycle - args.start_cycle ].referee.said ):

            # finish kick sequence by opp intercept
            if ( len( feat.kick_path_x ) > 0 ):
                feat.kick_cycle.append( cycle - args.start_cycle )
                feat.kick_path_x.append( wm[ cycle - args.start_cycle ].ball.pos.x )
                feat.kick_path_y.append( wm[ cycle - args.start_cycle ].ball.pos.y )
                feat.kicker.append( wm[ cycle - args.start_cycle ].last_kicker_unum + 1 )
                feat.receiver.append( 0 )
                ks.finishSequence( feat,  "bo--" )

            if ( not __debug__ ):
                if ( wm[ cycle - args.start_cycle ].dominate_side == "l" ):
                    print ("team r Intercept", cycle + 1 )
                elif ( wm[ cycle - args.start_cycle ].dominate_side == "r" ):
                    print ("team l Intercept", cycle + 1 )

        # same timimg kick( Penalty )
        elif ( kick_count > 1 and wm[cycle - args.start_cycle ].referee.said ):

            # finish kick sequence and play stopped
            if ( len( feat.kick_path_x ) > 0 ):
                feat.kick_cycle.append( cycle - args.start_cycle )
                feat.kick_path_x.append( wm[ cycle - args.start_cycle ].ball.pos.x )
                feat.kick_path_y.append( wm[ cycle - args.start_cycle ].ball.pos.y )
                feat.kicker.append( wm[ cycle - args.start_cycle ].last_kicker_unum + 1 )
                feat.receiver.append( 0 )
                ks.finishSequence( feat,  "bo--" )

            if ( not __debug__ ):
                # should be considered
                if ( wm[ cycle - args.start_cycle - 1 ].dominate_side == "l" ):
                    print ("team r Penalty", cycle + 1 )
                elif ( wm[ cycle - args.start_cycle - 1 ].dominate_side == "r" ):
                    print ("team l Penalty", cycle + 1 )

        elif ( kick_count == 1 and not wm[cycle - args.start_cycle ].referee.said ):
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


    l_disconnected_player = 0
    r_disconnected_player = 0
    for unum in range(11):
        if state.isDead( args.end_cycle, unum, 'l', wm ):
            l_disconnected_player = 1
        elif state.isDead( args.end_cycle,unum, 'r', wm ):
            r_disconnected_player = 1
    if team == 'l':
        feat.our_disconnected_player = l_disconnected_player
        feat.opp_disconnected_player = r_disconnected_player
    elif team == 'r':
        feat.our_disconnected_player = r_disconnected_player
        feat.opp_disconnected_player = l_disconnected_player

    feat.outputResult( args.filename, team )
    #feat.saveKickSequence( feat, outputKickedCycle=True )
    #ks.saveKickSequence( feat )
    #kd.saveKickDistribution( feat )

    if ( not __debug__ ):
        ks.printSequence( sp, feat )
        kd.printKickDistribution( sp, feat )
