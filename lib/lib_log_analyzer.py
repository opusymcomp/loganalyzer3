# ------library ------ #

import math

# index c

def calcRadian( x1, x2, y1, y2 ):

    return math.atan2( y2 - y1, x2 - x1 )


def changeRadianToDegree( radian ):

    return radian * 180 / math.pi


def countPlayOn( cycle1, cycle2, situation ):

    cnt = 0

    for i in range( cycle1, cycle2 ):
        if ( isPlayOn( i, situation ) ):
            cnt += 1

    return cnt


# index g


def getFileName( data ):

    return data.split( ".r" )[0]

def getResult( feat ):
    if ( feat.team_point[2] > feat.team_point[3] ):
        return 1
    else:
        return 0


def getTeamName( filename, side ):
    if ( side == "l" ):
        return filename.rsplit("/")[-1].split( "-vs-" )[0].split( "-", 1 )[1].rsplit( "_", 1 )[0]

    elif ( side == "r" ):
        return filename.rsplit("/")[-1].split( "-vs-" )[1].rsplit( "_", 1 )[0]


# index i

def isPlayOn( cycle, situation ):

    for i in range( len( situation ) - 1 ):

        if ( situation[i][0] < cycle and situation[i+1][0] > cycle ):

            if ( situation[i][1] == "t" ):
                return True

        elif ( situation[i][0] > cycle ):
            break


    return False



def isSameCycle( now_count, pre_count ):

    if ( now_count == pre_count ):
        return True
    else:
        return False


# index s

def selectTargetTeam( args ):

    l_teamname = getTeamName( getFileName( args.filename ), "l" )
    r_teamname = getTeamName( getFileName( args.filename ), "r" )

    if ( args.side == "l" ):
        return "l"

    elif ( args.side == "r" ):
        return "r"

    elif ( args.team == l_teamname ):
        return "l"

    elif ( args.team == r_teamname ):
        return "r"

    else:
        return "unknown"
