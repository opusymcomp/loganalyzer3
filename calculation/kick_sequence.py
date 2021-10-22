#!/usr/bin/env python
# cython: language_level=3
# -*- coding: utf-8 -*-

import cython
import itertools

from lib import lib_log_analyzer as lib
from lib import la_class

def appendSequence( feat: la_class.Feature, color: str, kick_dist_thr: cython.double ) -> None:
    INVALID_VALUE: cython.double = -10000.0

    START_SEQUENCE: cython.int = 0
    BETWEEN_SEQUENCE: cython.int = 1
    END_SEQUENCE: cython.int = -1

    POSITIVE_LABEL: cython.int = 1
    NEGATIVE_LABEL: cython.int = 0

    # ignore the kick_paths whose distance is shorter than kick_dist_thr
    tmp_kick_path_x: list = []
    tmp_kick_path_y: list = []

    # kick_sequence: ( [ kick_cycle, x, y, teacher signal, sequence flag, kicker_unum, receiver_unum, ...,
    # mate1_x, mate1_y, mate1_bodyangle, mate1_neckangle, ... , opp1_x, opp1_y, opp1_bodyangle, opp1_neckangle, ... ] )
    for i in range(len(feat.kick_path_x)):
        sequence_flag: cython.int = END_SEQUENCE if i == len(feat.kick_path_x) - 1 \
            else START_SEQUENCE if i == 0 \
            else BETWEEN_SEQUENCE
        label: cython.int = POSITIVE_LABEL if color == "ro-" \
            else NEGATIVE_LABEL if color == "bo--" \
            else -1
        if label == -1:
            raise SyntaxError
        if sequence_flag == BETWEEN_SEQUENCE:
            if lib.calcDistC(feat.kick_path_x[i], feat.kick_path_y[i], feat.kick_path_x[i-1], feat.kick_path_y[i-1]) < kick_dist_thr:
                continue

        tmp_kick_path_x.append(feat.kick_path_x[i])
        tmp_kick_path_y.append(feat.kick_path_y[i])

        tmp_kick_sequence: list = [feat.kick_cycle[i],
                                  feat.kick_path_x[i], feat.kick_path_y[i],
                                  label, sequence_flag,
                                  feat.kicker[i], feat.receiver[i]]

        if sequence_flag == END_SEQUENCE:
            # for teammate
            tmp_kick_sequence.extend([INVALID_VALUE for _ in range(11 * 4)])
            # for opponent
            tmp_kick_sequence.extend([INVALID_VALUE for _ in range(11 * 4)])
        else:
            # for teammate
            tmp_kick_sequence.extend(
                list(itertools.chain.from_iterable(
                    [feat.teammate_from_ball[i][j].pos.x, feat.teammate_from_ball[i][j].pos.y,
                     feat.teammate_from_ball[i][j].body_angle, feat.teammate_from_ball[i][j].neck_angle,
                     ] for j in range(11))))
            # for opponent
            tmp_kick_sequence.extend(
                list(itertools.chain.from_iterable(
                    [feat.opponent_from_ball[i][j].pos.x, feat.opponent_from_ball[i][j].pos.y,
                     feat.opponent_from_ball[i][j].body_angle, feat.opponent_from_ball[i][j].neck_angle,
                     ] for j in range(11))))

        feat.kick_sequence.append(tmp_kick_sequence)

    # used for plotting kick_sequences
    feat.all_kick_path_x.append( tmp_kick_path_x )
    feat.all_kick_path_y.append( tmp_kick_path_y )
    feat.color4plt_ks.append(color)
    # feat.color4plt_ks.append('ro-')


def printSequence(sp: la_class.ServerParam, feat: la_class.Feature, path: str) -> None:
    import matplotlib
    # smatplotlib.use('Agg')
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

    plt.xlim([-xlim, xlim])
    plt.ylim([ylim, -ylim])

    plt.tick_params(labelsize=32)

    # plot soccer fields
    plt.plot([sp.goal_line_l, -sp.penalty_area_x], [-sp.penalty_area_y, -sp.penalty_area_y], color='g', linewidth=4)
    plt.plot([sp.goal_line_l, -sp.penalty_area_x], [sp.penalty_area_y, sp.penalty_area_y], color='g', linewidth=4)
    plt.plot([sp.goal_line_r, sp.penalty_area_x], [-sp.penalty_area_y, -sp.penalty_area_y], color='g', linewidth=4)
    plt.plot([sp.goal_line_r, sp.penalty_area_x], [sp.penalty_area_y, sp.penalty_area_y], color='g', linewidth=4)
    plt.plot([-sp.penalty_area_x, -sp.penalty_area_x], [sp.penalty_area_y, -sp.penalty_area_y], color='g', linewidth=4)
    plt.plot([sp.penalty_area_x, sp.penalty_area_x], [sp.penalty_area_y, -sp.penalty_area_y], color='g', linewidth=4)

    plt.plot([sp.goal_line_l, sp.goal_line_r], [-sp.pitch_width / 2, -sp.pitch_width / 2], color='g', linewidth=4)
    plt.plot([sp.goal_line_l, sp.goal_line_r], [sp.pitch_width / 2, sp.pitch_width / 2], color='g', linewidth=4)
    plt.plot([sp.goal_line_l, sp.goal_line_l], [-sp.pitch_width / 2, sp.pitch_width / 2], color='g', linewidth=4)
    plt.plot([sp.goal_line_r, sp.goal_line_r], [-sp.pitch_width / 2, sp.pitch_width / 2], color='g', linewidth=4)

    plt.plot([0, 0], [-sp.pitch_width / 2, sp.pitch_width / 2], color='g', linewidth=4)
    p = plt.Circle((0.0, 0.0), 9.0, color='g', linewidth=4, fill=False)

    ax = plt.gca()
    ax.add_patch(p)

    for x, y, color in zip(feat.all_kick_path_x, feat.all_kick_path_y, feat.color4plt_ks):
        plt.plot(x, y, color)

    filename = path + feat.team_point[0] + "-kick_sequence"
    extension = [".eps", ".pdf", ".png", ".svg"]
    for e in extension:
        plt.savefig(filename + e, dpi=300, bbox_inches="tight", transparent=True)
    plt.show()


def finishSequence( feat: la_class.Feature, color: str, kick_dist_thr: cython.double ) -> None:
    appendSequence( feat, color, kick_dist_thr=kick_dist_thr )
    clearList( feat )


def clearList(feat: la_class.Feature) -> None:
    feat.kick_cycle = []
    feat.kick_path_x = []
    feat.kick_path_y = []
    feat.kicker = []
    feat.receiver = []
    feat.teammate_from_ball = []
    feat.opponent_from_ball = []


def getSequence( wm: list, sp: la_class.ServerParam, cycle: cython.int, feat: la_class.Feature, until_penalty_area: cython.bint = True, kick_dist_thr: cython.double = 3.0 ) -> cython.int:
    last_kick_side: cython.str = wm[cycle].dominate_side
    last_kick_cycle: cython.int = wm[cycle].last_kicked_cycle - 1

    kick_side: cython.str = wm[cycle + 1].dominate_side
    kick_cycle: cython.int = cycle

    NO_KICK: cython.int = -1
    NO_KICKER: cython.int = 0
    NO_RECEIVER: cython.int = 0

    if (kick_side == feat.target_team):

        kicked_from: cython.int = wm[cycle].last_kicker_unum + 1
        kicked_to: cython.int = wm[cycle + 1].last_kicker_unum + 1

        # Exit situations
        for i in range(last_kick_cycle, kick_cycle):

            for say in wm[i].referee.say:
                # considering own goal
                # last kick: our, kick_off: our -> own goal
                if ( "goal_" in say
                       and not "goal_kick_" in say ):
                    finishSequence( feat, "bo--", kick_dist_thr=kick_dist_thr )
                    return 0

        # attention to ball
        feat.kick_cycle.append(kick_cycle)
        feat.kick_path_x.append(wm[cycle].ball.pos.x)
        feat.kick_path_y.append(wm[cycle].ball.pos.y)
        if feat.target_team == "l":
            feat.teammate_from_ball.append(lib.sortPlayerUnumFromPos(wm[cycle].l.player, wm[cycle].ball.pos))
            feat.opponent_from_ball.append(lib.sortPlayerUnumFromPos(wm[cycle].r.player, wm[cycle].ball.pos))
        elif feat.target_team == "r":
            feat.teammate_from_ball.append(lib.sortPlayerUnumFromPos(wm[cycle].r.player, wm[cycle].ball.pos))
            feat.opponent_from_ball.append(lib.sortPlayerUnumFromPos(wm[cycle].l.player, wm[cycle].ball.pos))

        # start sequence
        if last_kick_side != feat.target_team:
            feat.kicker.append(NO_KICKER)
            feat.receiver.append(kicked_to)
        # continue sequence
        else:
            feat.kicker.append(kicked_from)
            feat.receiver.append(kicked_to)

        # Exit situations
        if feat.target_team == "l":
            if (wm[cycle].ball.pos.x > sp.penalty_area_x
                    and abs(wm[cycle].ball.pos.y) < sp.penalty_area_y):

                # isSequence
                if len( feat.kick_path_x ) > 1:
                    finishSequence( feat, "ro-", kick_dist_thr=kick_dist_thr ) if until_penalty_area else None
                    return 1

                # notSequence
                else:
                    clearList(feat)

        elif feat.target_team == "r":
            if (wm[cycle].ball.pos.x < - sp.penalty_area_x
                    and abs(wm[cycle].ball.pos.y) < sp.penalty_area_y):

                # isSequence
                if len( feat.kick_path_x ) > 1:
                    finishSequence( feat, "ro-", kick_dist_thr=kick_dist_thr ) if until_penalty_area else None
                    return 1

                # notSequence
                else:
                    clearList(feat)

    # Exit situations
    elif kick_side != feat.target_team:

        kicked_from: cython.int = wm[cycle].last_kicker_unum + 1
        kicked_to: cython.int = 0

        for i in range(last_kick_cycle, kick_cycle):

            # is sequence
            if len(feat.kick_path_x) > 0:
                for say in wm[i].referee.say:
                    # goal from out of target area
                    if "goal_" + feat.target_team in say:
                        feat.kick_cycle.append(NO_KICK)
                        feat.kick_path_x.append(wm[i].ball.pos.x)
                        feat.kick_path_y.append(wm[i].ball.pos.y)
                        feat.kicker.append(kicked_from)
                        feat.receiver.append(NO_RECEIVER)
                        finishSequence(feat, "ro-", kick_dist_thr=kick_dist_thr)
                        return 1

                    # goal_kick or corner_kick
                    # sequence end when ball leaves the pitch
                    if( "goal_kick_" in say
                        or "corner_kick_" in say
                        or "half_time" in say):
                        feat.kick_cycle.append( NO_KICK )
                        feat.kick_path_x.append( wm[i-1].ball.pos.x )
                        feat.kick_path_y.append( wm[i-1].ball.pos.y )
                        feat.kicker.append( kicked_from )
                        feat.receiver.append( NO_RECEIVER )
                        finishSequence( feat, "bo--", kick_dist_thr=kick_dist_thr )
                        return 0

                    # goalie catch
                    if "goalie_catch_" in say:
                        feat.kick_cycle.append(NO_KICK)
                        feat.kick_path_x.append(wm[i].ball.pos.x)
                        feat.kick_path_y.append(wm[i].ball.pos.y)
                        feat.kicker.append(kicked_from)
                        feat.receiver.append(NO_RECEIVER)
                        finishSequence(feat, "bo--", kick_dist_thr=kick_dist_thr)
                        return 0

        # isSequence and intercepted
        if ( len( feat.kick_path_x ) > 0 ):
            feat.kick_cycle.append( kick_cycle )
            feat.kick_path_x.append( wm[ cycle ].ball.pos.x )
            feat.kick_path_y.append( wm[ cycle ].ball.pos.y )
            feat.kicker.append( kicked_from )
            feat.receiver.append( NO_RECEIVER )
        finishSequence( feat, "bo--", kick_dist_thr=kick_dist_thr )

    return 0


def considerSimultaneousKick(wm: list, cycle: cython.int, feat: la_class.Feature, kick_dist_thr: cython.double = 3.0) -> None:
    if (len(feat.kick_path_x) > 0):
        feat.kick_cycle.append(cycle)
        feat.kick_path_x.append(wm[cycle].ball.pos.x)
        feat.kick_path_y.append(wm[cycle].ball.pos.y)
        feat.kicker.append(wm[cycle].last_kicker_unum + 1)
        feat.receiver.append(0)
        finishSequence(feat, "bo--", kick_dist_thr=kick_dist_thr)


def saveKickSequence(feat: la_class.Feature, path: str, outputKickedCycle: cython.bint = False) -> None:
    # kick_sequence data
    # named 'nn_kick_data.csv' before

    with open(path+'kick_sequence.csv', 'a') as f:
        for i in range(len(feat.kick_sequence)):
            if outputKickedCycle:
                f.write(str(feat.kick_sequence[i][0]) + ",")
            for j in range(1, len(feat.kick_sequence[i])):
                f.write(str(feat.kick_sequence[i][j]))
                if j == len(feat.kick_sequence[i]) - 1:
                    f.write("\n")
                else:
                    f.write(",")
