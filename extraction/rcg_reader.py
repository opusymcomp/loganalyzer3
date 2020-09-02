#!/usr/bin/env python


def getInformation( tmp_line, wm ):

    getBallInformation( tmp_line, wm )
    getLeftTeamInformation( tmp_line, wm )
    getRightTeamInformation( tmp_line, wm )



def getBallInformation( tmp_line, wm ):

    wm.ball.pos.x = float( tmp_line[3] )
    wm.ball.pos.y = float( tmp_line[4] )
    wm.ball.vel.x = float( tmp_line[5] )
    wm.ball.vel.y = float( tmp_line[6].strip(")") )



def getLeftTeamInformation( tmp_line, wm ):

    for unum in range(11):
        for j in range( len(tmp_line) - 19 ):
            if ( tmp_line[j] == '((l' and tmp_line[j+1] == str( unum + 1 ) + ')' ):
                wm.l.player[ unum ].hetero = int( tmp_line[j+2] )
                wm.l.player[ unum ].state = tmp_line[j+3]
                wm.l.player[ unum ].pos.x = float( tmp_line[j+4] )
                wm.l.player[ unum ].pos.y = float( tmp_line[j+5] )
                wm.l.player[ unum ].vel.x = float( tmp_line[j+6] )
                wm.l.player[ unum ].vel.y = float( tmp_line[j+7] )
                wm.l.player[ unum ].body_angle = float( tmp_line[j+8] )
                wm.l.player[ unum ].neck_angle = float( tmp_line[j+9] )
                # ignore pointto
                if ( tmp_line[j+12] == "(v" ):
                    wm.l.player[ unum ].view_area = int( tmp_line[j+14].strip(")") )
                    wm.l.player[ unum ].stamina = float( tmp_line[j+16] )
                    wm.l.player[ unum ].stamina_capacity = float( tmp_line[j+19].strip(")") )
                else:
                    wm.l.player[ unum ].view_area = int( tmp_line[j+12].strip(")") )
                    wm.l.player[ unum ].stamina = float( tmp_line[j+14] )
                    wm.l.player[ unum ].stamina_capacity = float( tmp_line[j+17].strip(")") )


def getRightTeamInformation( tmp_line, wm ):

    for unum in range(11):
        for j in range( len(tmp_line) - 19 ):
            if ( tmp_line[j] == '((r' and tmp_line[j+1] == str( unum + 1 ) + ')' ):
                wm.r.player[ unum ].hetero = int( tmp_line[j+2] )
                wm.r.player[ unum ].state = tmp_line[j+3]
                wm.r.player[ unum ].pos.x = float( tmp_line[j+4] )
                wm.r.player[ unum ].pos.y = float( tmp_line[j+5] )
                wm.r.player[ unum ].vel.x = float( tmp_line[j+6] )
                wm.r.player[ unum ].vel.y = float( tmp_line[j+7] )
                wm.r.player[ unum ].body_angle = float( tmp_line[j+8] )
                wm.r.player[ unum ].neck_angle = float( tmp_line[j+9] )
                # ignore pointto
                if ( tmp_line[j+12] == "(v" ):
                    wm.r.player[ unum ].view_area = int( tmp_line[j+14].strip(")") )
                    wm.r.player[ unum ].stamina = float( tmp_line[j+16] )
                    wm.r.player[ unum ].stamina_capacity = float( tmp_line[j+19].strip(")") )
                else:
                    wm.r.player[ unum ].view_area = int( tmp_line[j+12].strip(")") )
                    wm.r.player[ unum ].stamina = float( tmp_line[j+14] )
                    wm.r.player[ unum ].stamina_capacity = float( tmp_line[j+17].strip(")") )
