#!/usr/bin/env python
# cython: language_level=3

import cython

from lib import la_class


def getInformation( tmp_line: list, wm: la_class.WorldModel ) -> None:

    getBallInformation( tmp_line, wm )
    getLeftTeamInformation( tmp_line, wm )
    getRightTeamInformation( tmp_line, wm )


def getBallInformation( tmp_line: list, wm: la_class.WorldModel ) -> None:

    wm.ball.pos.x = float( tmp_line[3] )
    wm.ball.pos.y = float( tmp_line[4] )
    wm.ball.vel.x = float( tmp_line[5] )
    wm.ball.vel.y = float( tmp_line[6].strip(")") )


def getLeftTeamInformation( tmp_line: list, wm: la_class.WorldModel ) -> None:
    # get uniform number and geometrical informartion
    unum: cython.int = 0
    referred_i: cython.int = 0
    for i in range(len(tmp_line)):

        if tmp_line[i] == "((r":
            # skip
            break

        if "(" not in tmp_line[i]:
            # skip
            continue

        if tmp_line[i] == "((l":
            if referred_i > i:
                continue
            unum = int(tmp_line[i+1].replace(")", "")) - 1
            wm.l.player[unum].hetero = int(tmp_line[i+2])
            wm.l.player[unum].state = tmp_line[i+3]
            wm.l.player[unum].pos.x = float(tmp_line[i+4])
            wm.l.player[unum].pos.y = float(tmp_line[i+5])
            wm.l.player[unum].vel.x = float(tmp_line[i+6])
            wm.l.player[unum].vel.y = float(tmp_line[i+7])
            wm.l.player[unum].body_angle = float(tmp_line[i+8])
            wm.l.player[unum].neck_angle = float(tmp_line[i+9])
            if tmp_line[i+10] == "(v":
                referred_i = i + 10
                continue
            else:
                wm.l.player[unum].pointing_target.x = float(tmp_line[i+10])
                wm.l.player[unum].pointing_target.y = float(tmp_line[i+11])
                referred_i = i + 12
        if tmp_line[i] == "(v":
            wm.l.player[unum].quality = tmp_line[i+1]
            wm.l.player[unum].view_area = int(tmp_line[i+2].replace(")", ""))
            referred_i = i + 2
        if tmp_line[i] == "(s":
            wm.l.player[unum].stamina = float(tmp_line[i+1])
            wm.l.player[unum].effort = float(tmp_line[i+2])
            wm.l.player[unum].recovery = float(tmp_line[i+3])
            wm.l.player[unum].stamina_capacity = float(tmp_line[i+4].replace(")", ""))
            referred_i = i + 4
        if tmp_line[i] == "(f":
            wm.l.player[unum].focus_target = "{}_{}".format(tmp_line[i+1], tmp_line[i+2].replace(")", ""))
            referred_i = i + 2
        if tmp_line[i] == "(c":
            wm.l.player[unum].kick_count = int(tmp_line[i+1])
            wm.l.player[unum].dash_count = int(tmp_line[i+2])
            wm.l.player[unum].turn_count = int(tmp_line[i+3])
            wm.l.player[unum].catch_count = int(tmp_line[i+4])
            wm.l.player[unum].move_count = int(tmp_line[i+5])
            wm.l.player[unum].turn_neck_count = int(tmp_line[i+6])
            wm.l.player[unum].change_view_count = int(tmp_line[i+7])
            wm.l.player[unum].say_count = int(tmp_line[i+8])
            wm.l.player[unum].tackle_count = int(tmp_line[i+9])
            wm.l.player[unum].arm_target_count = int(tmp_line[i+10])
            wm.l.player[unum].attention_count = int(tmp_line[i+11].replace("))", ""))
            referred_i = i + 11



def getRightTeamInformation( tmp_line: list, wm: la_class.WorldModel ) -> None:
    unum: cython.int = 0
    referred_i: cython.int = 0
    is_left_team: cython.bint = False

    # get uniform number and geometrical information
    for i in range(len(tmp_line)):

        if tmp_line[i] == "((l":
            is_left_team = True
            continue

        if "(" not in tmp_line[i]:
            # skip
            continue

        if tmp_line[i] == "((r":
            is_left_team = False
            if referred_i > i:
                continue
            unum = int(tmp_line[i+1].replace(")", "")) - 1
            wm.r.player[unum].hetero = int(tmp_line[i+2])
            wm.r.player[unum].state = tmp_line[i+3]
            wm.r.player[unum].pos.x = float(tmp_line[i+4])
            wm.r.player[unum].pos.y = float(tmp_line[i+5])
            wm.r.player[unum].vel.x = float(tmp_line[i+6])
            wm.r.player[unum].vel.y = float(tmp_line[i+7])
            wm.r.player[unum].body_angle = float(tmp_line[i+8])
            wm.r.player[unum].neck_angle = float(tmp_line[i+9])
            if tmp_line[i+10] == "(v":
                referred_i = i + 10
                continue
            else:
                wm.r.player[unum].pointing_target.x = float(tmp_line[i+10])
                wm.r.player[unum].pointing_target.y = float(tmp_line[i+11])
                referred_i = i + 12
        if not is_left_team and tmp_line[i] == "(v":
            wm.r.player[unum].quality = tmp_line[i+1]
            wm.r.player[unum].view_area = int(tmp_line[i+2].replace(")", ""))
            referred_i = i + 2
        if not is_left_team and tmp_line[i] == "(s":
            wm.r.player[unum].stamina = float(tmp_line[i+1])
            wm.r.player[unum].effort = float(tmp_line[i+2])
            wm.r.player[unum].recovery = float(tmp_line[i+3])
            wm.r.player[unum].stamina_capacity = float(tmp_line[i+4].replace(")", ""))
            referred_i = i + 4
        if not is_left_team and tmp_line[i] == "(f":
            wm.r.player[unum].focus_target = "{}_{}".format(tmp_line[i+1], tmp_line[i+2])
            referred_i = i + 2
        if not is_left_team and tmp_line[i] == "(c":
            wm.r.player[unum].kick_count = int(tmp_line[i+1])
            wm.r.player[unum].dash_count = int(tmp_line[i+2])
            wm.r.player[unum].turn_count = int(tmp_line[i+3])
            wm.r.player[unum].catch_count = int(tmp_line[i+4])
            wm.r.player[unum].move_count = int(tmp_line[i+5])
            wm.r.player[unum].turn_neck_count = int(tmp_line[i+6])
            wm.r.player[unum].change_view_count = int(tmp_line[i+7])
            wm.r.player[unum].say_count = int(tmp_line[i+8])
            wm.r.player[unum].tackle_count = int(tmp_line[i+9])
            wm.r.player[unum].arm_target_count = int(tmp_line[i+10])
            wm.r.player[unum].attention_count = int(tmp_line[i+11].replace("))", "").replace(")", ""))
            referred_i = i + 11

