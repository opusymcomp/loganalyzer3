# This file is module of filename
# get an argument which is the name of target team
# then devide filename into target team and opponent team
# there are 4 return value [the name of target team , thename of opponent team , target team's score , opponent team's score ]


import glob  # need foor getting filename
import gzip

from lib import lib_log_analyzer as lib


def splitFileName(logname, l_teamname, r_teamname, team):
    left = str(logname.split("-vs-")[0].split("-", 1)[1].rsplit("_", 1)[0])
    right = str(logname.split("-vs-")[1].rsplit("_", 1)[0])
    l_score = logname.split("-vs-")[0].rsplit("_", 1)[1]
    r_score = logname.split("-vs-")[1].rsplit("_", 1)[1]
    l_ps_score = 0
    r_ps_score = 0

    if left != l_teamname and right != r_teamname:
        left = logname.split("-vs-")[0].split("-", 1)[1].rsplit("_", 2)[0]
        right = logname.split("-vs-")[1].rsplit("_", 2)[0]
        l_score = logname.split("-vs-")[0].rsplit("_", 2)[1]
        r_score = logname.split("-vs-")[1].rsplit("_", 2)[1]
        l_ps_score = logname.split("-vs-")[0].rsplit("_", 2)[2]
        r_ps_score = logname.split("-vs-")[1].rsplit("_", 2)[2]
        if left != l_teamname or right != r_teamname:
            raise SyntaxError("team names are not matched...")

    if team == "l":
        return [left, right, int(l_score), int(r_score), int(l_ps_score), int(r_ps_score)]

    elif team == "r":
        return [right, left, int(r_score), int(l_score), int(r_ps_score), int(l_ps_score)]

    else:
        print("emergency error : file name doesn't correspond to rcg file")
        return ["0", "0", 0, 0, 0, 0]
