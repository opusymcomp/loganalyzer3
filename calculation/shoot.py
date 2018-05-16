# -*- coding: utf-8 -*-
# hori

import math
import re

from lib import lib_log_analyzer as lib

def sucShoot( side, kick, goal ):

    cnt = 0
    cycle = -1
    lastKicker = []

    for g in goal:
        if( g[1] == team ):
            for k in kick:
                if( k[1] < g[0] ):
                    if( cycle != k[1] ):
                        lastKicker = []
                    lastKicker.append( k )
                    cycle = k[1]
                else:
                    break
            for lk in lastKicker:
                if( lk[0] == g[1] ):
                    cnt += 1
                    break

    return cnt



def isOurShoot( wm, sp, cycle, side ):

    x = wm.ball.pos.x
    y = wm.ball.pos.y
    xv = wm.ball.vel.x
    yv = wm.ball.vel.y

    if ( side == 'l' ):
        while x < sp.goal_line_r and ( xv ** 2 + yv ** 2 ) > 1:
            x = x + xv
            y = y + yv
            xv = xv * sp.ball_speed_decay
            yv = yv * sp.ball_speed_decay
            if x >= sp.goal_line_r and y > - ( sp.goal_post ) and y < sp.goal_post:
                if ( not __debug__ ):
                    print ( "our", wm.last_kicker_unum+1, "shoot!:", cycle + 1 )
                return True

    elif( side == 'r' ):
        while x > sp.goal_line_l and ( xv ** 2 + yv ** 2 ) > 1:
            x = x + xv
            y = y + yv
            xv = xv * sp.ball_speed_decay
            yv = yv * sp.ball_speed_decay
            if x <= sp.goal_line_l and y > - ( sp.goal_post ) and y < sp.goal_post:
                if ( not __debug__ ):
                    print ( "our", wm.last_kicker_unum+1, "shoot!:", cycle + 1 )
                return True
    return False


def isOppShoot( wm, sp, cycle, side ):

    x = wm.ball.pos.x
    y = wm.ball.pos.y
    xv = wm.ball.vel.x
    yv = wm.ball.vel.y

    if ( side == 'l' ):
        opp_side = 'r'
    elif ( side == 'r' ):
        opp_side = 'l'

    if ( opp_side == 'l' ):
        while x < sp.goal_line_r and ( xv ** 2 + yv ** 2 ) > 1:
            x = x + xv
            y = y + yv
            xv = xv * sp.ball_speed_decay
            yv = yv * sp.ball_speed_decay
            if x >= sp.goal_line_r and y > - ( sp.goal_post ) and y < sp.goal_post:
                if ( not __debug__ ):
                    print ( "opp", wm.last_kicker_unum+1, "shoot!:", cycle + 1 )
                return True

    elif( opp_side == 'r' ):
        while x > sp.goal_line_l and ( xv ** 2 + yv ** 2 ) > 1:
            x = x + xv
            y = y + yv
            xv = xv * sp.ball_speed_decay
            yv = yv * sp.ball_speed_decay
            if x <= sp.goal_line_l and y > - ( sp.goal_post ) and y < sp.goal_post:
                if ( not __debug__ ):
                    print ( "opp", wm.last_kicker_unum+1, "shoot!:", cycle + 1 )
                return True
    return False
