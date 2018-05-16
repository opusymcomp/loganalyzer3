from extraction import get_tackle as gt


def isFinish( kick, situation, tackle, player_state_l, player_state_r, index, team ):

    if index == len( kick ) - 1:
        return False

    start_cycle = kick[index][1]
    end_cycle = kick[index + 1][1]

    if kick[index][0] != kick[index + 1][0] or kick[index][0] != team:
        return False

    # ----- check pass is consecutive or not ----- #

    for i in range( len( situation ) ):
        if situation[i][1] == "f" and situation[i][0] > start_cycle and situation[i][0] < end_cycle:
            return False

    for i in range( len( tackle ) ):
        if tackle[i][0] > start_cycle and tackle[i][0] < end_cycle and  gt.checkTackle( i, tackle, player_state_l, player_state_r ):
            return False

    # ------------------------------------- #

    return True

def createSequence( kick, situation, tackle, player_state_l, player_state_r, team ):

    sequence = [] # contain sequences
    tmp_sequence = [] # represent a sequence by kick seriese

    for i in range( len( kick ) ):

        if kick[i][0] == team:
            tmp_sequence.append( kick[i] )

        if not isFinish( kick, situation, tackle, player_state_l, player_state_r, i, team ): # if kick other team or change mode, finish sequence
            sequence.append( tmp_sequence )
            tmp_sequence = []

    return sequence

def isPenaltyArea( ball, sequence, team ):

    if len( sequence ) <= 1: # if the sequence is short
        return False


    for i in sequence: # loop kick in a sequence
        cycle = i[1]
        if ( ball[cycle - 1][0] > 36.0 and ball[cycle - 1][1] < 20.16 and ball[cycle - 1][1] > -20.16 ) and team == "l":
            return True

        if ( ball[cycle - 1][0] < -36.0 and ball[cycle - 1][1] < 20.16 and ball[cycle - 1][1] > -20.16 ) and team == "r":
            return True

    return False

def countPenaltyArea( ball, kick, situation, tackle, player_state_l, player_state_r, team ):

    sequences = [] # contain sequences, a sequence represent one action seriese
    count = 0 # the number of penetrating opp penalty area

    sequences = createSequence( kick, situation, tackle, player_state_l, player_state_r, team )

    seq = []

    for sq in sequences:
        if isPenaltyArea( ball, sq, team ):
            count += 1

    return count
