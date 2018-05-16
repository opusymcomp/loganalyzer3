# -*- coding: utf-8 -*-
#! /usr/bin/env python

from matplotlib import pyplot as plt


def printSequence( sp ):
    xlim = sp.pitch_length / 2 + 5.0
    ylim = sp.pitch_width / 2 + 5.0
    plt.xlim( [-xlim, xlim] )
    plt.ylim( [ylim, -ylim] )
    plt.tick_params(labelsize=32)

    # plot soccer fields
    plt.plot( [ sp.goal_line_l, -sp.penalty_area_x ], [ -sp.penalty_area_y, -sp.penalty_area_y ], color='g', linewidth=4 )
    plt.plot( [ sp.goal_line_l, -sp.penalty_area_x ], [ sp.penalty_area_y, sp.penalty_area_y ], color='g', linewidth=4 )
    plt.plot( [ sp.goal_line_r, sp.penalty_area_x ], [ -sp.penalty_area_y, -sp.penalty_area_y ], color='g', linewidth=4 )
    plt.plot( [ sp.goal_line_r, sp.penalty_area_x ], [ sp.penalty_area_y, sp.penalty_area_y ], color='g', linewidth=4 )
    plt.plot( [ -sp.penalty_area_x, -sp.penalty_area_x ], [ sp.penalty_area_y, -sp.penalty_area_y ], color='g', linewidth=4 )
    plt.plot( [ sp.penalty_area_x, sp.penalty_area_x ], [ sp.penalty_area_y, -sp.penalty_area_y ], color='g', linewidth=4 )

    plt.plot( [ sp.goal_line_l, sp.goal_line_r ], [ -sp.pitch_width / 2, -sp.pitch_width / 2 ], color='g', linewidth=4 )
    plt.plot( [ sp.goal_line_l, sp.goal_line_r ], [ sp.pitch_width / 2, sp.pitch_width / 2 ], color='g', linewidth=4 )
    plt.plot( [ sp.goal_line_l, sp.goal_line_l ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], color='g', linewidth=4 )
    plt.plot( [ sp.goal_line_r, sp.goal_line_r ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], color='g', linewidth=4 )

    plt.plot( [ 0, 0 ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], color='g', linewidth=4 )
    p = plt.Circle((0.0, 0.0), 9.0, color='g', linewidth=4, fill=False)

    ax = plt.gca()
    ax.add_patch(p)

    plt.show()

def finishSequence( feat, color ):

    plt.plot( feat.kick_path_x, feat.kick_path_y, color )

    feat.kick_path_x = []
    feat.kick_path_y = []


def getSequence( wm, sp, cycle, team, feat ):

    last_kick_side = wm[cycle+1].dominate_side
    last_kick_cycle = wm[cycle+1].last_kicked_cycle - 1

    kick_cycle = cycle

    if ( last_kick_side == team ):

        # attention to ball
        feat.kick_path_x.append( wm[ last_kick_cycle ].ball.pos.x )
        feat.kick_path_y.append( wm[ last_kick_cycle ].ball.pos.y )

        # Exit situations
        for i in range( last_kick_cycle, kick_cycle ):
            for say in wm[i].referee.say:
                if ( "goal_" in say ):
                    feat.kick_path_x.append( wm[i].ball.pos.x )
                    feat.kick_path_y.append( wm[i].ball.pos.y )
                    finishSequence( feat, "ro-" )
                    return 1


        # Exit situations
        if ( wm[ last_kick_cycle ].ball.pos.x > sp.penalty_area_x and \
             abs( wm[ last_kick_cycle ].ball.pos.y ) < sp.penalty_area_y ):

            # isSequence
            if ( len( feat.kick_path_x ) > 1  ):
                finishSequence( feat, "ro-" )
                return 1

            # notSequence
            else:
                feat.kick_path_x = []
                feat.kick_path_y = []

    # Exit situations
    elif ( last_kick_side != team ):
        # opponent kick
        finishSequence( feat, "bo-" )



    return 0
