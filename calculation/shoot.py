#!/usr/bin/env python
# cython: language_level=3
# -*- coding: utf-8 -*-

# implemented by Hori

import cython

from lib import la_class

def isOurShoot( wm: la_class.WorldModel, sp: la_class.ServerParam, cycle: cython.int, side: str ) -> cython.bint:

    x: cython.double = wm.ball.pos.x
    y: cython.double = wm.ball.pos.y
    xv: cython.double = wm.ball.vel.x
    yv: cython.double = wm.ball.vel.y

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


def isOppShoot( wm: la_class.WorldModel, sp: la_class.ServerParam, cycle: cython.int, side: str ) -> cython.bint:

    x: cython.double = wm.ball.pos.x
    y: cython.double = wm.ball.pos.y
    xv: cython.double = wm.ball.vel.x
    yv: cython.double = wm.ball.vel.y

    if ( side == 'l' ):
        opp_side: cython.str = 'r'
    elif ( side == 'r' ):
        opp_side: cython.str = 'l'

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
