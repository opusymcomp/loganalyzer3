#!/usr/bin/env python
# cython: language_level=3

cdef class Feature:
    cdef str logname
    cdef str target_team
    cdef list index
    cdef list kick_cycle
    cdef list kick_path_x
    cdef list kick_path_y
    cdef list all_kick_path_x
    cdef list all_kick_path_y
    cdef list color4plt_ks
    cdef list teammate_from_ball
    cdef list opponent_from_ball
    cdef list kicker
    cdef list receiver
    cdef list kick_sequence
    cdef list team_point
    cdef str date
    cdef int final_result
    cdef int our_yellow
    cdef int opp_yellow
    cdef int our_tackle
    cdef int all_our_tackle
    cdef int opp_tackle
    cdef int all_opp_tackle
    cdef int our_shoot
    cdef int opp_shoot
    cdef int our_dominate_time
    cdef int opp_dominate_time
    cdef double our_possession
    cdef double opp_possession
    cdef list our_kick
    cdef list opp_kick
    cdef list our_pass
    cdef list opp_pass
    cdef list pass_propability
    cdef int our_through_pass
    cdef int opp_through_pass
    cdef int penalty_area
    cdef int our_point
    cdef int opp_point
    cdef int our_dribble
    cdef int opp_dribble
    # cdef int our_dribble_dist
    # cdef int opp_dribble_dist
    cdef int our_penalty_area
    cdef int opp_penalty_area
    cdef int our_disconnected_player
    cdef int opp_disconnected_player


    # cdef __init__(self)
    cdef void outputIndexForIR(self, int start, int end)
    cdef void outputIndexForR(self, str filename, str side)
    cdef void outputIntegrateResult(self, int start, int end)
    cdef void outputResult(self, str filename, str side)


cdef class Team:
    cdef str name
    cdef list player
    cdef double offsideLineX

    # cdef __init__(self, str teamname)


cdef class Player:
    cdef int hetero
    cdef str state
    cdef Position pos
    cdef Position vel
    cdef double body_angle
    cdef double neck_angle
    cdef int view_area
    cdef int stamina
    cdef int stamina_capacity
    cdef str action

    # cdef __init__(self)


cdef class Position:
    cdef double x
    cdef double y

    # cdef __init__(self)


cdef class Ball:
    cdef Position pos
    cdef Position vel

    # cdef __init__(self)


cdef class Referee:
    cdef str playmode
    cdef list say
    cdef bint said

    # cdef __init__(self)


cdef class ServerParam:
    cdef double pitch_length
    cdef double pitch_width
    cdef double goal_line_l
    cdef double goal_line_r
    cdef int goal_post
    cdef double penalty_area_x
    cdef double penalty_area_y
    cdef double ball_speed_decay
    cdef list hetero

    # cdef __init__(self)


cdef class HeteroParam:
    cdef double player_speed_max
    cdef double stamina_inc_max
    cdef double player_decay
    cdef double inertia_moment
    cdef double dash_power_rate
    cdef double player_size
    cdef double kickable_margin
    cdef double kick_land
    cdef double extra_stamina
    cdef double effort_max
    cdef double effort_min
    cdef double kick_power_rate
    cdef double foul_detect_probability
    cdef double catchable_area_l_stretch

    # cdef __init__(self)


cdef class WorldModel:
    cdef Ball ball
    cdef Team l
    cdef Team r
    cdef Referee referee
    cdef str dominate_side
    cdef int last_kicker_unum
    cdef int last_kicked_cycle

    # cdef __init__(self, str team_l, str team_r)

