import math

def vec_dist( pos1, pos2 ):

    return  math.sqrt( pow( pos1[0] - pos2[0], 2.0 ) + pow( pos1[1] - pos2[1], 2.0 ) )

#####################################

def get_nearest_player( ball_pos, player_pos ):

    min_dist = 10000000.0;
    nearest_player = -1

    for i in range( len( player_pos ) ):
        tmp_dist = vec_dist( ball_pos, player_pos[i] )
        if tmp_dist < min_dist:
            nearest_player = i#player_pos[i]

    return nearest_player

#####################################

def nearestPlayerFromBall( ball, pos_l, pos_r ):

    nearest_list = []
    for i in range( len( ball ) ):
        tmp = []
        tmp.append( get_nearest_player( ball[i], pos_l[i] ) )
        tmp.append( get_nearest_player( ball[i], pos_r[i] ) )
        nearest_list.append( tmp )

    return nearest_list
