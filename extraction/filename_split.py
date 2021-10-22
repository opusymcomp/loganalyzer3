#!/usr/bin/env python
# cython: language_level=3

import cython

# This file is module of filename
# get an argument which is the name of target team
# then devide filename into target team and opponent team
# there are 4 return value [the name of target team , thename of opponent team , target team's score , opponent team's score ]


def splitFileName(logname: str, l_teamname: str, r_teamname: str, team: str) -> list:
    left: cython.str = str(logname.split("-vs-")[0].split("-", 1)[1].rsplit("_", 1)[0])
    right: cython.str = str(logname.split("-vs-")[1].rsplit("_", 1)[0])
    l_score: cython.str = logname.split("-vs-")[0].rsplit("_", 1)[1]
    r_score: cython.str = logname.split("-vs-")[1].rsplit("_", 1)[1]
    l_ps_score: cython.str = "0"
    r_ps_score: cython.str = "0"

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
        return ["none", "none", 0, 0, 0, 0]
