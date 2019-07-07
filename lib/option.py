from . import lib_log_analyzer as lib

import argparse
import os

def parser():
    usage = 'python main.py <file name> [--side <l or r>] [--team <teamname>] [--help]'
    parser = argparse.ArgumentParser( usage=usage )
    parser.add_argument( "filename" )
    parser.add_argument( "-s", "--side", \
                         default=None, \
                         help="select target team side" )
    parser.add_argument( "-t", "--team",\
                         default=None, \
                         help="select target team name")
    parser.add_argument( "-g", "--game", \
                         action="store_true", \
                         default=False, \
                         help="output csv file about the game(cycle, playmode, coordinate)")
    parser.add_argument( "-r", \
                         action="store_true", \
                         default=False, \
                         help="directory mode")
    parser.add_argument( "--without-index", \
                         action="store_true", \
                         default=False, \
                         help="output without index")
    parser.add_argument( "--each-cycle", \
                         action="store_true", \
                         default=False, \
                         help="output result for each cycle")
    parser.add_argument( "--start-cycle", \
                         type=int, \
                         default=0, \
                         help="start cycle")
    parser.add_argument( "--end-cycle", \
                         type=int, \
                         default=6000, \
                         help="end cycle")

    #print (parser.parse_args())
    return parser.parse_args()
