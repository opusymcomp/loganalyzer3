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


def analyzeLog(args, wm, sp, feat):

    # write index
    if not args.without_index:
        feat.outputIndexForR(feat.team_point[0]) if feat.target_team == 'l' else feat.outputIndexForR(feat.team_point[1])

    ol.calcOffsideLine(args, wm)

    for cycle in range(args.start_cycle, args.end_cycle):

        relative_cycle = cycle - args.start_cycle

        for say in wm[relative_cycle].referee.say:
            if ("offside" in say
                    or "free_kick_" in say
                    or "kick_in_" in say
                    or "before_kick_off" in say
                    or "kick_off" in say
                    or "foul_charge_" in say
                    or "goal_kick_" in say
                    or "goalie_catch_ball_" in say
                    or "corner_kick_" in say
                    or "drop_ball" in say):
                wm[relative_cycle].dominate_side = "neutral"
                wm[relative_cycle].referee.said = True

            elif "goal_l" in say:
                wm[relative_cycle].dominate_side = "neutral"
                wm[relative_cycle].referee.said = True
                if not __debug__:
                    print("team l goal!")
                if feat.target_team == "l":
                    feat.our_point += 1
                elif feat.target_team == "r":
                    feat.opp_point += 1

            elif "goal_r" in say:
                wm[relative_cycle].dominate_side = "neutral"
                wm[relative_cycle].referee.said = True
                if not __debug__:
                    print("team r goal!")
                if feat.target_team == "r":
                    feat.our_point += 1
                elif feat.target_team == "l":
                    feat.opp_point += 1

        if (wm[relative_cycle].dominate_side == "l"
                and wm[relative_cycle].referee.playmode == "play_on"):
            if feat.target_team == "l":
                feat.our_dominate_time += 1
            if feat.target_team == "r":
                feat.opp_dominate_time += 1

        if (wm[relative_cycle].dominate_side == "r"
                and wm[relative_cycle].referee.playmode == "play_on"):
            if feat.target_team == "r":
                feat.our_dominate_time += 1
            if feat.target_team == "l":
                feat.opp_dominate_time += 1

        try:
            feat.our_possession = float(feat.our_dominate_time / float(feat.our_dominate_time + feat.opp_dominate_time))
            feat.opp_possession = float(feat.opp_dominate_time / float(feat.our_dominate_time + feat.opp_dominate_time))
        except ZeroDivisionError:
            feat.our_possession = 0
            feat.opp_possession = 0

        feat.our_yellow += referee.countOurYellowCard(wm[relative_cycle], feat.target_team)
        feat.opp_yellow += referee.countOppYellowCard(wm[relative_cycle], feat.target_team)

        feat.all_our_tackle += gt.countOurTackle(wm[relative_cycle], feat.target_team)
        feat.all_opp_tackle += gt.countOppTackle(wm[relative_cycle], feat.target_team)
        feat.our_tackle += gt.countOurSuccessTackle(wm[relative_cycle], wm[relative_cycle + 1],
                                                    feat.target_team)
        feat.opp_tackle += gt.countOppSuccessTackle(wm[relative_cycle], wm[relative_cycle + 1],
                                                    feat.target_team)

        kick_count = gk.isKick(wm,  relative_cycle)

        # simultaneous kick
        if kick_count > 1:
            ks.considerSimultaneousKick(wm, relative_cycle, feat, kick_dist_thr=0.0)
            # finish kick sequence by opp intercept
            if not __debug__ and not wm[relative_cycle].referee.said:
                if wm[relative_cycle].dominate_side == "l":
                    print("team r Intercept", cycle + 1)
                elif wm[relative_cycle].dominate_side == "r":
                    print("team l Intercept", cycle + 1)
            # finish kick sequence by penalty and play stopped
            if not __debug__ and wm[relative_cycle].referee.said:
                # should be considered
                if wm[relative_cycle - 1].dominate_side == "l":
                    print("team r Penalty", cycle + 1)
                elif wm[relative_cycle - 1].dominate_side == "r":
                    print("team l Penalty", cycle + 1)
        elif (kick_count == 1
              and not wm[relative_cycle].referee.said):
            if shoot.isOurShoot(wm[relative_cycle + 1], sp, cycle, feat.target_team):
                feat.our_shoot += 1
            elif shoot.isOppShoot(wm[relative_cycle + 1], sp, cycle, feat.target_team):
                feat.opp_shoot += 1
            direction = pc.countKick(wm,  relative_cycle, feat)
            pc.countPass(wm, relative_cycle, direction, feat)
            tp.countThroughPass(wm, relative_cycle, feat)
            dc.countDribble(wm, relative_cycle, feat)
            feat.our_penalty_area += ks.getSequence(wm, sp, relative_cycle, feat,
                                                    until_penalty_area=True, kick_dist_thr=0.0)

        # find disconnected player
        l_disconnected_player = 0
        r_disconnected_player = 0
        for unum in range(11):
            if state.isDead(relative_cycle, unum, 'l', wm):
                l_disconnected_player += 1
            elif state.isDead(relative_cycle, unum, 'r', wm):
                r_disconnected_player += 1
        if feat.target_team == 'l':
            feat.our_disconnected_player = max(l_disconnected_player, feat.our_disconnected_player)
            feat.opp_disconnected_player = max(r_disconnected_player, feat.opp_disconnected_player)
        elif feat.target_team == 'r':
            feat.our_disconnected_player = max(r_disconnected_player, feat.our_disconnected_player)
            feat.opp_disconnected_player = max(l_disconnected_player, feat.opp_disconnected_player)

        # output for each cycle
        if args.each_cycle:
            if not args.without_index:
                feat.outputIndexForIR(args.start_cycle+1, cycle+1)
            feat.outputIntegrateResult(args.start_cycle+1, cycle+1)

    feat.outputResult( feat.team_point[0] )
    # ks.saveKickSequence( feat, outputKickedCycle=True )
    # kd.saveKickDistribution( feat, degree_range=90 )

    if not __debug__:
        ks.printSequence(sp, feat)
        kd.printKickDistribution(sp, feat)
