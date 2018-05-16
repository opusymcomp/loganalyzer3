#!/usr/bin/env python

import sys

from lib import option
from lib import lib_log_analyzer as lib
from lib import la_class

from extraction import extract
from extraction import filename_split as fns
from calculation import calculate as calc
from calculation import dribble_count as dc

#from extraction  import kick_txt as txt
#from lib import distribution3dplot as plot

if __name__ == "__main__":

    # ------ options ------ #

    args = option.parser()

    if ( args.r ):
        print ( "please use loop.sh" )
        sys.exit()

    print ( "loganalyzer3" )


    # ------ target team side ------ #

    team = lib.selectTargetTeam( args )

    if ( team == "unknown" ):
        print ( "\n(Error Message) select target team. \nplease command with --help" )
        sys.exit()

    # ------ initialization ------ #

    wm = []

    for i in range( args.start_cycle, args.end_cycle+1 ):
        wm.append( la_class.WorldModel( lib.getTeamName( args.filename, "l" ), \
                                           lib.getTeamName( args.filename, "r" ) ) )

    sp = la_class.ServerParam()
    feature = la_class.Feature()

    # ------ extraction ------ #

    extract.extractRcg( args, wm, sp )
    extract.extractRcl( args, wm, sp )

    feature.date = lib.getFileName( args.filename ).split('-')[0].split('/')[-1]
    feature.team_point = fns.splitFileName( args.filename, team )
    feature.final_result = lib.getResult( feature )
    feature.team = team

    # ------ calculation ------ #

    calc.analyzeLog( args, wm, sp, feature, team )

    # ------ They are under development. ------ #

    #pass_probability = pb.passProbability( ball, kick, situation, tackle, player_state_l, player_state_r, team )

    #txt.KickTxt( data, date )
    #plot.Plot3d( date )
