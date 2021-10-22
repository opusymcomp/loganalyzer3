#!/usr/bin/env python
# cython: language_level=3

import cython

from lib import la_class


def getHetero( line: str, h_id: cython.int, sp: la_class.ServerParam ) -> None:

    tmp: list = line.split(")(")

    sp.hetero_params[h_id].player_speed_max = float( tmp[1].split()[1] )
    sp.hetero_params[h_id].stamina_inc_max = float( tmp[2].split()[1] )
    sp.hetero_params[h_id].player_decay = float( tmp[3].split()[1] )
    sp.hetero_params[h_id].inertia_moment = float( tmp[4].split()[1] )
    sp.hetero_params[h_id].dash_power_rate = float( tmp[5].split()[1] )
    sp.hetero_params[h_id].player_size = float( tmp[6].split()[1] )
    sp.hetero_params[h_id].kick_land = float( tmp[8].split()[1] )
    sp.hetero_params[h_id].extra_stamina = float( tmp[9].split()[1] )
    sp.hetero_params[h_id].effort_max = float( tmp[10].split()[1] )
    sp.hetero_params[h_id].effort_min = float( tmp[11].split()[1] )
    sp.hetero_params[h_id].kick_power_rate = float( tmp[12].split()[1] )
    sp.hetero_params[h_id].foul_detect_probability = float( tmp[13].split()[1] )
    sp.hetero_params[h_id].catchable_area_l_stretch = float( tmp[14].split()[1].strip("))") )
