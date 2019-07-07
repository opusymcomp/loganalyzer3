# -*- coding: utf-8 -*-
#! /usr/bin/env python

from lib import lib_log_analyzer as lib

def appendSequence( feat, color ):

    INVALID_VALUE = -10000.0

    START_SEQUENCE = 0
    BETWEEN_SEQUENCE = 1
    END_SEQUENCE = -1

    POSITIVE_LABEL = 1
    NEGATIVE_LABEL = 0

    # kick_sequence( [ kick_cycle, x, y, teacher signal, sequence flag, kicker_unum, receiver_unum, opp1_x, opp1_y, ... ] )

    for i in range( len( feat.kick_path_x ) ):
        if ( i == len( feat.kick_path_x ) - 1 ):
            if ( color == "ro-" ):
                feat.kick_sequence.append( [ feat.kick_cycle[i], \
                                             feat.kick_path_x[i], feat.kick_path_y[i], \
                                             POSITIVE_LABEL, END_SEQUENCE, \
                                             feat.kicker[i], feat.receiver[i], \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE ] )
            elif ( color == "bo--" ):
                feat.kick_sequence.append( [ feat.kick_cycle[i], \
                                             feat.kick_path_x[i], feat.kick_path_y[i], \
                                             NEGATIVE_LABEL, END_SEQUENCE, \
                                             feat.kicker[i], feat.receiver[i], \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE, \
                                             INVALID_VALUE, INVALID_VALUE ] )
        elif ( i == 0 ):
            if ( color == "ro-" ):
                feat.kick_sequence.append( [ feat.kick_cycle[i], \
                                             feat.kick_path_x[i], feat.kick_path_y[i], \
                                             POSITIVE_LABEL, START_SEQUENCE, \
                                             feat.kicker[i], feat.receiver[i], \
                                             feat.opponent_from_ball[i][0].pos.x, feat.opponent_from_ball[i][0].pos.y, \
                                             feat.opponent_from_ball[i][1].pos.x, feat.opponent_from_ball[i][1].pos.y, \
                                             feat.opponent_from_ball[i][2].pos.x, feat.opponent_from_ball[i][2].pos.y, \
                                             feat.opponent_from_ball[i][3].pos.x, feat.opponent_from_ball[i][3].pos.y, \
                                             feat.opponent_from_ball[i][4].pos.x, feat.opponent_from_ball[i][4].pos.y, \
                                             feat.opponent_from_ball[i][5].pos.x, feat.opponent_from_ball[i][5].pos.y, \
                                             feat.opponent_from_ball[i][6].pos.x, feat.opponent_from_ball[i][6].pos.y, \
                                             feat.opponent_from_ball[i][7].pos.x, feat.opponent_from_ball[i][7].pos.y, \
                                             feat.opponent_from_ball[i][8].pos.x, feat.opponent_from_ball[i][8].pos.y, \
                                             feat.opponent_from_ball[i][9].pos.x, feat.opponent_from_ball[i][9].pos.y, \
                                             feat.opponent_from_ball[i][10].pos.x, feat.opponent_from_ball[i][10].pos.y ] )
            elif ( color == "bo--" ):
                feat.kick_sequence.append( [ feat.kick_cycle[i], \
                                             feat.kick_path_x[i], feat.kick_path_y[i], \
                                             NEGATIVE_LABEL, START_SEQUENCE, \
                                             feat.kicker[i], feat.receiver[i], \
                                             feat.opponent_from_ball[i][0].pos.x, feat.opponent_from_ball[i][0].pos.y, \
                                             feat.opponent_from_ball[i][1].pos.x, feat.opponent_from_ball[i][1].pos.y, \
                                             feat.opponent_from_ball[i][2].pos.x, feat.opponent_from_ball[i][2].pos.y, \
                                             feat.opponent_from_ball[i][3].pos.x, feat.opponent_from_ball[i][3].pos.y, \
                                             feat.opponent_from_ball[i][4].pos.x, feat.opponent_from_ball[i][4].pos.y, \
                                             feat.opponent_from_ball[i][5].pos.x, feat.opponent_from_ball[i][5].pos.y, \
                                             feat.opponent_from_ball[i][6].pos.x, feat.opponent_from_ball[i][6].pos.y, \
                                             feat.opponent_from_ball[i][7].pos.x, feat.opponent_from_ball[i][7].pos.y, \
                                             feat.opponent_from_ball[i][8].pos.x, feat.opponent_from_ball[i][8].pos.y, \
                                             feat.opponent_from_ball[i][9].pos.x, feat.opponent_from_ball[i][9].pos.y, \
                                             feat.opponent_from_ball[i][10].pos.x, feat.opponent_from_ball[i][10].pos.y ] )
        else:
            if ( color == "ro-" ):
                feat.kick_sequence.append( [ feat.kick_cycle[i], \
                                             feat.kick_path_x[i], feat.kick_path_y[i], \
                                             POSITIVE_LABEL, BETWEEN_SEQUENCE, \
                                             feat.kicker[i], feat.receiver[i], \
                                             feat.opponent_from_ball[i][0].pos.x, feat.opponent_from_ball[i][0].pos.y, \
                                             feat.opponent_from_ball[i][1].pos.x, feat.opponent_from_ball[i][1].pos.y, \
                                             feat.opponent_from_ball[i][2].pos.x, feat.opponent_from_ball[i][2].pos.y, \
                                             feat.opponent_from_ball[i][3].pos.x, feat.opponent_from_ball[i][3].pos.y, \
                                             feat.opponent_from_ball[i][4].pos.x, feat.opponent_from_ball[i][4].pos.y, \
                                             feat.opponent_from_ball[i][5].pos.x, feat.opponent_from_ball[i][5].pos.y, \
                                             feat.opponent_from_ball[i][6].pos.x, feat.opponent_from_ball[i][6].pos.y, \
                                             feat.opponent_from_ball[i][7].pos.x, feat.opponent_from_ball[i][7].pos.y, \
                                             feat.opponent_from_ball[i][8].pos.x, feat.opponent_from_ball[i][8].pos.y, \
                                             feat.opponent_from_ball[i][9].pos.x, feat.opponent_from_ball[i][9].pos.y, \
                                             feat.opponent_from_ball[i][10].pos.x, feat.opponent_from_ball[i][10].pos.y ] )
            elif ( color == "bo--" ):
                feat.kick_sequence.append( [ feat.kick_cycle[i], \
                                             feat.kick_path_x[i], feat.kick_path_y[i], \
                                             NEGATIVE_LABEL, BETWEEN_SEQUENCE, \
                                             feat.kicker[i], feat.receiver[i], \
                                             feat.opponent_from_ball[i][0].pos.x, feat.opponent_from_ball[i][0].pos.y, \
                                             feat.opponent_from_ball[i][1].pos.x, feat.opponent_from_ball[i][1].pos.y, \
                                             feat.opponent_from_ball[i][2].pos.x, feat.opponent_from_ball[i][2].pos.y, \
                                             feat.opponent_from_ball[i][3].pos.x, feat.opponent_from_ball[i][3].pos.y, \
                                             feat.opponent_from_ball[i][4].pos.x, feat.opponent_from_ball[i][4].pos.y, \
                                             feat.opponent_from_ball[i][5].pos.x, feat.opponent_from_ball[i][5].pos.y, \
                                             feat.opponent_from_ball[i][6].pos.x, feat.opponent_from_ball[i][6].pos.y, \
                                             feat.opponent_from_ball[i][7].pos.x, feat.opponent_from_ball[i][7].pos.y, \
                                             feat.opponent_from_ball[i][8].pos.x, feat.opponent_from_ball[i][8].pos.y, \
                                             feat.opponent_from_ball[i][9].pos.x, feat.opponent_from_ball[i][9].pos.y, \
                                             feat.opponent_from_ball[i][10].pos.x, feat.opponent_from_ball[i][10].pos.y ] )


def printSequence( sp, feat ):

    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt
    import matplotlib.font_manager as fm

    fig = plt.figure(figsize=(10.5, 6.8))
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    xlim = sp.pitch_length / 2 + 5.0
    ylim = sp.pitch_width / 2 + 5.0
    fm._rebuild()

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

    for x, y, color in zip( feat.all_kick_path_x, feat.all_kick_path_y, feat.color4plt_ks ):
        plt.plot( x, y, color )

    filename= feat.team_point[0] + "-kick_sequence"
    extension = [".eps", ".pdf", ".png", ".svg"]
    for e in extension:
        plt.savefig(filename+e, dpi=300, bbox_inches="tight", transparent=True)
    #plt.show()

def finishSequence( feat, color ):

    feat.all_kick_path_x.append( feat.kick_path_x )
    feat.all_kick_path_y.append( feat.kick_path_y )
    feat.color4plt_ks.append(color)
    #feat.color4plt_ks.append('ro-')

    appendSequence( feat, color )
    clearList( feat )

def clearList( feat ):

    feat.kick_cycle = []
    feat.kick_path_x = []
    feat.kick_path_y = []
    feat.kicker = []
    feat.receiver = []
    feat.opponent_pos = []

def getSequence( wm, sp, cycle, team, feat ):

    last_kick_side = wm[cycle].dominate_side
    last_kick_cycle = wm[cycle].last_kicked_cycle - 1

    kick_side = wm[cycle+1].dominate_side
    kick_cycle = cycle

    NO_KICK = -1
    NO_KICKER = 0
    NO_RECEIVER = 0

    if ( kick_side == team ):

        kicked_from = wm[cycle].last_kicker_unum + 1
        kicked_to = wm[cycle+1].last_kicker_unum + 1

        # Exit situations
        for i in range( last_kick_cycle, kick_cycle ):

            for say in wm[i].referee.say:

                # goal from out of penalty area
                if ( "goal_" + team in say ):
                    feat.kick_cycle.append( NO_KICK )
                    feat.kick_path_x.append( wm[i].ball.pos.x )
                    feat.kick_path_y.append( wm[i].ball.pos.y )
                    feat.kicker.append( kicked_from )
                    feat.receiver.append( NO_RECEIVER )
                    finishSequence( feat, "ro-" )
                    return 1

                # considering own goal
                elif ( "goal_" in say \
                       and not "goal_kick_" in say ):
                    finishSequence( feat, "bo--" )
                    return 0

        # attention to ball
        feat.kick_cycle.append( kick_cycle )
        feat.kick_path_x.append( wm[ cycle ].ball.pos.x )
        feat.kick_path_y.append( wm[ cycle ].ball.pos.y )
        if ( team == "l" ):
            feat.opponent_from_ball.append( lib.sortPlayerUnumFromPos( wm[ cycle ].r.player, wm[ cycle ].ball.pos ) )
        elif ( team == "r" ):
            feat.opponent_from_ball.append( lib.sortPlayerUnumFromPos( wm[ cycle ].l.player, wm[ cycle ].ball.pos ) )

        # start sequence
        if ( last_kick_side != team ):
            feat.kicker.append( NO_KICKER )
            feat.receiver.append( kicked_to )
        # continue sequence
        else:
            feat.kicker.append( kicked_from )
            feat.receiver.append( kicked_to )

        # Exit situations
        if ( wm[ cycle ].ball.pos.x > sp.penalty_area_x and \
             abs( wm[ cycle ].ball.pos.y ) < sp.penalty_area_y ):

            # isSequence
            if ( len( feat.kick_path_x ) > 1 ):
                finishSequence( feat, "ro-" )
                return 1

            # notSequence
            else:
                clearList( feat )

    # Exit situations
    elif ( kick_side != team ):

        kicked_from = wm[cycle].last_kicker_unum+1
        kicked_to = 0

        # goal_kick or corner_kick
        for i in range( last_kick_cycle, kick_cycle ):

            for say in wm[i].referee.say:
                # sequence end when ball leaves the pitch
                if( "goal_kick_" in say \
                    or "corner_kick_" in say ):
                    feat.kick_cycle.append( NO_KICK )
                    feat.kick_path_x.append( wm[i-1].ball.pos.x )
                    feat.kick_path_y.append( wm[i-1].ball.pos.y )
                    feat.kicker.append( kicked_from )
                    feat.receiver.append( NO_RECEIVER )
                    finishSequence( feat, "bo--" )

        # isSequence and intercepted
        if ( len( feat.kick_path_x ) > 0 ):
            feat.kick_cycle.append( kick_cycle )
            feat.kick_path_x.append( wm[ cycle ].ball.pos.x )
            feat.kick_path_y.append( wm[ cycle ].ball.pos.y )
            feat.kicker.append( kicked_from )
            feat.receiver.append( NO_RECEIVER )
        finishSequence( feat, "bo--" )

    return 0





def saveKickSequence(feat, outputKickedCycle=False):

    # kick_sequence data
    # named 'nn_kick_data.csv' before

    with open('kick_sequence.csv', 'a') as f:
        for i in range( len(feat.kick_sequence) ):
            if ( outputKickedCycle ):
                f.write( str( feat.kick_sequence[i][0] ) + "," )
            for j in range( 1, len( feat.kick_sequence[i] ) ):
                f.write( str( feat.kick_sequence[i][j] ) )
                if ( j == len( feat.kick_sequence[i] ) - 1 ):
                    f.write( "\n" )
                else:
                    f.write( "," )
