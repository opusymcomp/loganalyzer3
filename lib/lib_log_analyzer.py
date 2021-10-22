#!/usr/bin/env python
# cython: language_level=3

import math
import cython
import argparse

from lib import la_class

# index c

def calcDist(pos1: la_class.Position, pos2: la_class.Position) -> cython.double:

    return math.sqrt(math.pow((pos1.x - pos2.x), 2) + math.pow((pos1.y - pos2.y), 2))


def calcDistC(x1: cython.double, y1: cython.double, x2: cython.double, y2: cython.double) -> cython.double:

    return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))


def calcRadian(pos1: la_class.Position, pos2: la_class.Position) -> cython.double:

    return math.atan2(pos2.y - pos1.y, pos2.x - pos1.x)


def calcRadianC(x1: cython.double, y1: cython.double, x2: cython.double, y2: cython.double) -> cython.double:

    return math.atan2(y2 - y1, x2 - x1)


def changeRadianToDegree(radian: cython.double) -> cython.double:

    return radian * 180 / math.pi


def countPlayOn(cycle1: cython.int, cycle2: cython.int, situation: list) -> cython.int:

    cnt: cython.int = 0

    for i in range(cycle1, cycle2):
        if isPlayOn(i, situation):
            cnt += 1

    return cnt


# index g

def getFileName(data: str) -> str:

    return data.split(".r")[0]


def getResult(feat: la_class.Feature) -> cython.int:
    # compare the results of normal (and extra) halves
    if feat.team_point[2] > feat.team_point[3]:
        return 3
    elif feat.team_point[2] < feat.team_point[3]:
        return 0
    else:
        # compare the results of penalty shootouts
        if feat.team_point[4] > feat.team_point[5]:
            return 3
        elif feat.team_point[4] < feat.team_point[5]:
            return 0
    # draw game
    return 1


# index i

def isPlayOn(cycle: cython.int, situation: list) -> cython.bint:

    for i in range(len(situation) - 1):

        if situation[i][0] < cycle < situation[i+1][0]:

            if situation[i][1] == "t":
                return True

        elif situation[i][0] > cycle:
            break

    return False


def isSameCycle(now_count: cython.int, pre_count: cython.int) -> cython.bint:

    if now_count == pre_count:
        return True
    else:
        return False


# index s

def selectTargetTeam(args: argparse.Namespace, l_teamname: str, r_teamname: str) -> str:
    if args.side == "l":
        return "l"

    elif args.side == "r":
        return "r"

    elif args.team == l_teamname:
        return "l"

    elif args.team == r_teamname:
        return "r"

    else:
        return "unknown"


def sortPlayerUnumFromPos(player_list: list, target_pos: la_class.Position) -> list:
    return sorted(player_list, key=lambda player: calcDist(player.pos, target_pos))
