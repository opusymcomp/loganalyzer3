import math
from extraction import get_tackle as gt


def isLongKick( ball, kick, index ):

    start_cycle = kick[index][1]
    end_cycle = kick[index + 1][1]

    dist = math.sqrt ( pow( ball[start_cycle - 1][0] - ball[end_cycle - 1][0], 2.0 ) + pow( ball[start_cycle - 1][1] - ball[end_cycle - 1][1], 2.0 ) )

    if kick[index][2] == kick[index + 1][2] and kick[index][0] == kick[index + 1][0]:
        return False

    if dist < 2.0:
        return False

    return True

def passChecker( kick, index, team ):

    if kick[index][0] == kick[index + 1][0] and kick[index][2] != kick[index + 1][2] and kick[index][0] == team:
        return True

    return False


def exceptionPass( ball, kick, situation, tackle, player_state_l, player_state_r, index, team ):

    if index == len( kick ) - 1:
        return False

    start_cycle = kick[index][1]
    end_cycle = kick[index + 1][1]

    if kick[index][0] != team:
        return False

    if not isLongKick( ball, kick, index ):
        return False

    # ----- check pass is consecutive or not ----- #

    for i in range( len( situation ) ):
        if situation[i][1] == "f" and situation[i][0] > start_cycle and situation[i][0] < end_cycle:
            return False

    for i in range( len( tackle ) ):
        if tackle[i][0] > start_cycle and tackle[i][0] < end_cycle and gt.checkTackle( i, tackle, player_state_l, player_state_r ):
            return False

    # ------------------------------------- #

    return True

def checkPassSuccess( ball, kick, miss, success, index, team ):

    start_cycle = kick[index][1]
    end_cycle = kick[index + 1][1]

    if team == "l":
        if not passChecker( kick, index, team ):
            miss[0] += 1
            if( ball[start_cycle - 1][0] > 36.0 and ball[start_cycle - 1][1] < 20.16 and ball[start_cycle - 1][1] > -20.16 ):
                miss[1] += 1
            elif ball[start_cycle - 1][0] > 17.5:
                miss[2] += 1
            elif ball[start_cycle - 1][0] > -17.5:
                miss[3] += 1
            else:
                miss[4] += 1

            return False
        else:
            success[0] += 1
            if( ball[start_cycle - 1][0] > 36.0 and ball[start_cycle - 1][1] < 20.16 and ball[start_cycle - 1][1] > -20.16 ):
                success[1] += 1
            elif ball[start_cycle - 1][0] > 17.5:
                success[2] += 1
            elif ball[start_cycle - 1][0] > -17.5:
                success[3] += 1
            else:
                success[4] += 1

            return True

    else:
        if not passChecker( kick, index, team ):
            miss[0] += 1
            if( ball[start_cycle - 1][0] < -36.0 and ball[start_cycle - 1][1] < 20.16 and ball[start_cycle - 1][1] > -20.16 ):
                miss[1] += 1
            elif ball[start_cycle - 1][0] < -17.5:
                miss[2] += 1
            elif ball[start_cycle - 1][0] < 17.5:
                miss[3] += 1
            else:
                miss[4] += 1

            return False
        else:
            success[0] += 1
            if( ball[start_cycle - 1][0] < -36.0 and ball[start_cycle - 1][1] < 20.16 and ball[start_cycle - 1][1] > -20.16 ):
                success[1] += 1
            elif ball[start_cycle - 1][0] < -17.5:
                success[2] += 1
            elif ball[start_cycle - 1][0] < 17.5:
                success[3] += 1
            else:
                success[4] += 1

            return True

def passProbability( ball, kick, situation, tackle, player_state_l, player_state_r, team ):

    # success = [ pass_success, pass_success_pa, pass_success_at, pass_success_mt, pass_success_dt ]
    # miss = [ pass_miss, pass_miss_pa, pass_miss_at, pass_miss_mt, pass_miss_dt ]
    # probability = [ all, pa, at, mt, dt ]
    success = []
    miss = []
    probability = []
    count = 0 # the number of pass


    for i in range( 5 ):
        success.append( 0 )
        miss.append( 0 )
        probability.append( 0 )

    for i in range( len( kick ) ):

        if not exceptionPass( ball, kick, situation, tackle, player_state_l, player_state_r, i, team ):
            continue

        count += 1

        checkPassSuccess( ball, kick, miss, success, i, team )

    for i in range( 5 ):
        if success[i] == 0:
            probability[i] = 0
        else:
            probability[i] = round( success[i] / float( success[i] + miss[i] ), 2 )

    return probability
