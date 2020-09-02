#!/usr/bin/env python

import sys

from lib import option
from lib import la_class

from extraction import extract
from calculation import calculate as calc

#from extraction  import kick_txt as txt
#from lib import distribution3dplot as plot

if __name__ == "__main__":

    # ------ options ------ #
    args = option.parser()

    if ( args.r ):
        print ( "please use loop.sh" )
        sys.exit()

    # ------ initialization ------ #

    wm = []

    for i in range( args.start_cycle, args.end_cycle+1 ):
        wm.append(la_class.WorldModel("left", "right"))

    sp = la_class.ServerParam()
    feature = la_class.Feature()

    # ------ extraction ------ #

    extract.extractRcg( args, wm, sp, feature )
    extract.extractRcl( args, wm, sp )

    # ------ calculation ------ #

    calc.analyzeLog( args, wm, sp, feature )

    #pass_probability = pb.passProbability( ball, kick, situation, tackle, player_state_l, player_state_r, team )

    #txt.KickTxt( data, date )
    #plot.Plot3d( date )
