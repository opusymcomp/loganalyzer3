#!/usr/bin/env python

import os

from . import rcg_reader as rcg
from . import rcl_reader as rcl
from . import hetero
from . import referee

from . import filename_split as fns

from lib import lib_log_analyzer as lib

import gzip


def extractRcg(args, wm, sp, feature):
    cycle = 0
    current_play_mode = "unknown"

    filename = lib.getFileName(args.filename)
    if os.path.isfile(filename + ".rcg.gz"):
        filename += ".rcg.gz"
    elif os.path.isfile(filename + ".rcg"):
        filename += ".rcg"
    else:
        raise FileNotFoundError(filename + ".rcg.gz or " + filename + ".rcg")

    try:
        f = gzip.open(filename, "rt")
        # try seek
        f.seek(1)
        f.seek(0)
    except OSError:
        f = open(filename, "r")

    for line in f:
        if "(team 1 " in line:
            l_teamname, r_teamname = line.split()[2:4]
            feature.target_team = lib.selectTargetTeam(args, l_teamname, r_teamname)

        if "(player_type (id" in line:
            hetero_id = int(line.split()[2].strip(")(player_speed_max"))
            hetero.getHetero(line, hetero_id, sp)

        if "(playmode" in line:
            current_play_mode = referee.getCurrentPlayMode(line)

        if "(show" in line:
            tmp_line = line.split()

            # consider analyze cycles
            if args.start_cycle > int(tmp_line[1]):
                continue
            elif args.end_cycle < int(tmp_line[1]):
                continue

            if not lib.isSameCycle(int(tmp_line[1]), cycle):
                cycle = int(tmp_line[1])

                rcg.getInformation(tmp_line, wm[cycle - args.start_cycle])
                referee.setPlayMode(current_play_mode, wm[cycle - args.start_cycle])

                if cycle == 2999:
                    cycle += 1
                    rcg.getInformation(tmp_line, wm[cycle - args.start_cycle])
                    wm[cycle - args.start_cycle].referee.playmode = "time_over"

        if "(msg" in line and "(result" in line:
            tmp_result = line.split()
            feature.date = tmp_result[4]
            feature.logname = tmp_result[4] + "-" + tmp_result[5].strip(")\"")
            feature.team_point = fns.splitFileName(feature.logname, l_teamname, r_teamname, feature.target_team)
            feature.final_result = lib.getResult(feature)

    # file close
    f.close()

    # team name update
    for i in wm:
        i.l.name = l_teamname
        i.r.name = r_teamname


def extractRcl(args, wm, sp):
    filename = lib.getFileName(args.filename)
    if os.path.isfile(filename + ".rcl.gz"):
        filename += ".rcl.gz"
    elif os.path.isfile(filename + ".rcl"):
        filename += ".rcl"
    else:
        raise FileNotFoundError(filename + ".rcl.gz or " + filename + ".rcl")

    try:
        f = gzip.open(filename, "rt")
        # try seek
        f.seek(1)
        f.seek(0)
    except OSError:
        f = open(filename, "r")

    for line in f:
        # consider analyze cycles
        if args.start_cycle > int(line.split()[0].split(",")[0]):
            continue
        elif args.end_cycle < int(line.split()[0].split(",")[0]):
            continue

        # initial position
        if args.start_cycle == 0:
            rcl.getInitialPosition(line, wm[0])

        # getActions( Only playon )
        if lib.isSameCycle(int(line.split()[0].split(",")[1]), 0):

            # ignore coach and referee
            if (not "_Coach" in line \
                    and not "(referee" in line):
                cycle = int(line.split()[0].split(",")[0])
                rcl.getAction(line, wm[cycle - args.start_cycle])

        if "(referee" in line:
            cycle = int(line.split()[0].split(",")[0])
            referee.sayMessage(line, wm[cycle - args.start_cycle])

    # file close
    f.close()
