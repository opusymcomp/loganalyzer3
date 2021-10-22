#!/usr/bin/env python
# cython: language_level=3

import os
import glob
import cython
import argparse
import traceback

from lib import option
from lib import la_class

from extraction import extract
from calculation import calculate as calc


def doAnalyze(filename: str, args:argparse.Namespace) -> None:
    print(filename)

    # ------ initialization ------ #

    wm: list = []

    for _ in range( args.start_cycle, args.end_cycle+1 ):
        wm.append(la_class.WorldModel("left", "right"))

    sp: la_class.ServerParam = la_class.ServerParam()
    feature: la_class.Feature = la_class.Feature()

    # ------ extraction ------ #

    extract.extractRcg( filename, args, wm, sp, feature )
    if feature.team_point[0] == 'none' and feature.team_point[1] == 'none':
        print("Neither is the target team name. skip...")
        return

    extract.extractRcl( filename, args, wm, sp )

    # ------ calculation ------ #

    calc.analyzeLog( args, wm, sp, feature )

    #pass_probability = pb.passProbability( ball, kick, situation, tackle, player_state_l, player_state_r, team )


if __name__ == "__main__":

    # ------ options ------ #
    args: argparse.Namespace = option.parser()
    os.makedirs(args.output_dir, exist_ok=True)

    # ------ for directory ------ #
    if os.path.isdir(args.filename):
        filepath: str = args.filename if args.filename[-1] == "/" else '{}/'.format(args.filename)
        for f in sorted(glob.glob(filepath+'*.rcg*')):
            try:
                doAnalyze(f, args)
            except:
                traceback.print_exc()
    # ------ for single file ------ #
    else:
        doAnalyze(args.filename, args)
