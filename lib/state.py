#!/usr/bin/env python

def isGoalie( cycle, unum, side, wm ):

    if ( side == "l" ):
        if( int( wm[cycle].l.player[unum].state, 16 ) & int( 0x00000008 ) == 8 ):
            return True
        else:
            return False

    elif ( side == "r"):
        if( int( wm[cycle].r.player[unum].state, 16 ) & int( 0x00000008 ) == 8 ):
            return True
        else:
            return False

def isDead( cycle, unum, side, wm ):

    if ( side == 'l' ):
        if ( wm[cycle].l.player[unum].state == '0' ):
            return True
        else:
            return False

    elif ( side == 'r' ):
        if ( wm[cycle].r.player[unum].state == '0' ):
            return True
        else:
            return False


def checkTackle( state ):
    if ( int( state, 16 ) & int( 0x00002000 ) == 8192 ):
        return False
    else:
        return True


def checkKick( wm, unum, side ):

    if ( side == "l" ):
        if ( int( wm.l.player[unum].state, 16 ) & int( 0x00000004 ) == 4 ):
            return False

        else:
            return True

    elif ( side == "r" ):
        if ( int( wm.r.player[unum].state, 16 ) & int( 0x00000004 ) == 4 ):
            return False

        else:
            return True
