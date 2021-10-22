#!/usr/bin/env python
# cython: language_level=3

import os
import csv
import cython
import itertools

@cython.cclass
class Position:
    x = cython.declare(cython.double, visibility='public')
    y = cython.declare(cython.double, visibility='public')
    def __init__(self) -> None:
        self.x = 0.0
        self.y = 0.0


@cython.cclass
class Ball:
    pos = cython.declare(Position, visibility='public')
    vel = cython.declare(Position, visibility='public')
    def __init__(self) -> None:
        self.pos = Position()
        self.vel = Position()


@cython.cclass
class Referee:
    playmode = cython.declare(str, visibility='public')
    say = cython.declare(list, visibility='public')
    said = cython.declare(cython.bint, visibility='public')
    def __init__(self) -> None:
        self.playmode = ""
        self.say = []
        self.said = False


@cython.cclass
class HeteroParam:
    player_speed_max = cython.declare(cython.double, visibility='public')
    stamina_inc_max = cython.declare(cython.double, visibility='public')
    player_decay = cython.declare(cython.double, visibility='public')
    inertia_moment = cython.declare(cython.double, visibility='public')
    dash_power_rate = cython.declare(cython.double, visibility='public')
    player_size = cython.declare(cython.double, visibility='public')
    kickable_margin = cython.declare(cython.double, visibility='public')
    kick_land = cython.declare(cython.double, visibility='public')
    extra_stamina = cython.declare(cython.double, visibility='public')
    effort_max = cython.declare(cython.double, visibility='public')
    effort_min = cython.declare(cython.double, visibility='public')
    kick_power_rate = cython.declare(cython.double, visibility='public')
    foul_detect_probability = cython.declare(cython.double, visibility='public')
    catchable_area_l_stretch = cython.declare(cython.double, visibility='public')

    def __init__(self) -> None:
        self.player_speed_max = 1.05
        self.stamina_inc_max = 45.0
        self.player_decay = 0.4
        self.inertia_moment = 5.0
        self.dash_power_rate = 0.006
        self.player_size = 0.3
        self.kickable_margin = 0.7
        self.kick_land = 0.1
        self.extra_stamina = 50.0
        self.effort_max = 1.0
        self.effort_min = 0.6
        self.kick_power_rate = 0.027
        self.foul_detect_probability = 0.5
        self.catchable_area_l_stretch = 1.0


@cython.cclass
class ServerParam:
    pitch_length = cython.declare(cython.double, visibility='readonly')
    pitch_width = cython.declare(cython.double, visibility='readonly')
    goal_line_l = cython.declare(cython.double, visibility='readonly')
    goal_line_r = cython.declare(cython.double, visibility='readonly')
    goal_post = cython.declare(cython.int, visibility='readonly')
    penalty_area_x = cython.declare(cython.double, visibility='readonly')
    penalty_area_y = cython.declare(cython.double, visibility='readonly')
    ball_speed_decay = cython.declare(cython.double, visibility='readonly')
    hetero_params = cython.declare(list, visibility='public')

    def __init__(self) -> None:
        self.pitch_length = 105.0
        self.pitch_width = 68.0
        self.goal_line_l = -52.5
        self.goal_line_r = 52.5
        self.goal_post = 7
        self.penalty_area_x = 36.05
        self.penalty_area_y = 20.00
        self.ball_speed_decay = 0.94
        self.hetero_params = []
        for i in range(18):
            self.hetero_params.append(HeteroParam())


@cython.cclass
class Player:
    hetero = cython.declare(cython.int, visibility='public')
    state = cython.declare(str, visibility='public')
    pos = cython.declare(Position, visibility='public')
    vel = cython.declare(Position, visibility='public')
    body_angle = cython.declare(cython.double, visibility='public')
    neck_angle = cython.declare(cython.double, visibility='public')
    pointing_target = cython.declare(Position, visibility='public')
    quality = cython.declare(str, visibility='public')
    view_area = cython.declare(cython.int, visibility='public')
    stamina = cython.declare(cython.double, visibility='public')
    effort = cython.declare(cython.double, visibility='public')
    recovery = cython.declare(cython.double, visibility='public')
    stamina_capacity = cython.declare(cython.double, visibility='public')
    focus_target = cython.declare(str, visibility='public')
    kick_count = cython.declare(cython.int, visibility='public')
    dash_count = cython.declare(cython.int, visibility='public')
    turn_count = cython.declare(cython.int, visibility='public')
    catch_count = cython.declare(cython.int, visibility='public')
    move_count = cython.declare(cython.int, visibility='public')
    turn_neck_count = cython.declare(cython.int, visibility='public')
    change_view_count = cython.declare(cython.int, visibility='public')
    say_count = cython.declare(cython.int, visibility='public')
    tackle_count = cython.declare(cython.int, visibility='public')
    arm_target_count = cython.declare(cython.int, visibility='public')
    attention_count = cython.declare(cython.int, visibility='public')
    action = cython.declare(str, visibility='public')

    def __init__(self) -> None:
        self.hetero = -1
        self.state = "0x1"
        self.pos = Position()
        self.vel = Position()
        self.body_angle = 0.0
        self.neck_angle = 0.0
        self.pointing_target = Position()
        self.quality = "none"
        self.view_area = 0
        self.stamina = 8000.0
        self.effort = 0.0
        self.recovery = 0.0
        self.stamina_capacity = 130600.0
        self.focus_target = "none"
        self.kick_count = 0
        self.dash_count = 0
        self.turn_count = 0
        self.catch_count = 0
        self.move_count = 0
        self.turn_neck_count = 0
        self.change_view_count = 0
        self.say_count = 0
        self.tackle_count = 0
        self.arm_target_count = 0
        self.attention_count = 0
        self.action = ""


@cython.cclass
class Team:
    name = cython.declare(str, visibility='public')
    player = cython.declare(list, visibility='public')
    offsideLineX = cython.declare(cython.double, visibility='public')

    def __init__(self) -> None:
        self.name = ""
        self.player = []
        for i in range(11):
            self.player.append(Player())
        self.offsideLineX = 0.0


@cython.cclass
class WorldModel:
    ball = cython.declare(Ball, visibility='public')
    l = cython.declare(Team, visibility='public')
    r = cython.declare(Team, visibility='public')
    referee = cython.declare(Referee, visibility='public')
    dominate_side = cython.declare(str, visibility='public')
    last_kicker_unum = cython.declare(cython.int, visibility='public')
    last_kicked_cycle = cython.declare(cython.int, visibility='public')

    def __init__(self, team_l: str, team_r: str) -> None:
        self.ball = Ball()
        self.l = Team()
        self.l.name = team_l
        self.r = Team()
        self.r.name = team_r
        self.referee = Referee()
        self.dominate_side = "none"
        self.last_kicker_unum = -1
        self.last_kicked_cycle = -1

    def outputInfo(self, fname: str) -> None:
        mode: str = 'a' if os.path.exists(fname) else 'w'
        all_info: list = [
            'ball_pos_x',
            'ball_pos_y',
            'ball_vel_x',
            'ball_vel_y'
        ]
        players_info: list = [
            'hetero_id',
            'status',
            'pos_x',
            'pos_y',
            'vel_x',
            'vel_y',
            'body_angle',
            'neck_angle',
            'pointing_x',
            'pointing_y',
            'quality',
            'view_area',
            'stamina',
            'effort',
            'recovery',
            'stamina_capacity',
            'focus_target',
            'kick_count',
            'dash_count',
            'turn_count',
            'catch_count',
            'move_count',
            'turn_neck_count',
            'change_view_count',
            'say_count',
            'tackle_count',
            'arm_target_count',
            'attention_count',
            'action'
        ]
        for s in ['l', 'r']:
            for unum in range(1, 12):
                for p in players_info:
                    all_info.append('{}{}_{}'.format(s, unum, p))

        with open(fname, mode) as f:
            csv_writer = csv.writer(f)

            # add column values
            if mode == 'w':
                csv_writer.writerow(all_info)

            row: list = [
                self.ball.pos.x,
                self.ball.pos.y,
                self.ball.vel.x,
                self.ball.vel.y
            ]
            row.extend(list(itertools.chain.from_iterable(
                       [[p.hetero,
                         p.state,
                         p.pos.x,
                         p.pos.y,
                         p.vel.x,
                         p.vel.y,
                         p.body_angle,
                         p.neck_angle,
                         p.pointing_target.x,
                         p.pointing_target.y,
                         p.quality,
                         p.view_area,
                         p.stamina,
                         p.effort,
                         p.recovery,
                         p.stamina_capacity,
                         p.focus_target,
                         p.kick_count,
                         p.dash_count,
                         p.turn_count,
                         p.catch_count,
                         p.move_count,
                         p.turn_neck_count,
                         p.change_view_count,
                         p.say_count,
                         p.tackle_count,
                         p.arm_target_count,
                         p.attention_count,
                         p.action] for p in self.l.player])))
            row.extend(list(itertools.chain.from_iterable(
                       [[p.hetero,
                         p.state,
                         p.pos.x,
                         p.pos.y,
                         p.vel.x,
                         p.vel.y,
                         p.body_angle,
                         p.neck_angle,
                         p.pointing_target.x,
                         p.pointing_target.y,
                         p.quality,
                         p.view_area,
                         p.stamina,
                         p.effort,
                         p.recovery,
                         p.stamina_capacity,
                         p.focus_target,
                         p.kick_count,
                         p.dash_count,
                         p.turn_count,
                         p.catch_count,
                         p.move_count,
                         p.turn_neck_count,
                         p.change_view_count,
                         p.say_count,
                         p.tackle_count,
                         p.arm_target_count,
                         p.attention_count,
                         p.action] for p in self.r.player])))

            csv_writer.writerow(row)

@cython.cclass
class Feature:
    logname = cython.declare(str, visibility='public')
    target_team = cython.declare(str, visibility='public')
    index = cython.declare(list, visibility='public')

    kick_cycle = cython.declare(list, visibility='public')
    kick_path_x = cython.declare(list, visibility='public')
    kick_path_y = cython.declare(list, visibility='public')
    all_kick_path_x = cython.declare(list, visibility='public')
    all_kick_path_y = cython.declare(list, visibility='public')
    color4plt_ks = cython.declare(list, visibility='public')
    teammate_from_ball = cython.declare(list, visibility='public')
    opponent_from_ball = cython.declare(list, visibility='public')
    kicker = cython.declare(list, visibility='public')
    receiver = cython.declare(list, visibility='public')
    kick_sequence = cython.declare(list, visibility='public')

    team_point = cython.declare(list, visibility='public')
    date = cython.declare(str, visibility='public')
    final_result = cython.declare(cython.int, visibility='public')
    our_yellow = cython.declare(cython.int, visibility='public')
    opp_yellow = cython.declare(cython.int, visibility='public')
    our_tackle = cython.declare(cython.int, visibility='public')
    all_our_tackle = cython.declare(cython.int, visibility='public')
    opp_tackle = cython.declare(cython.int, visibility='public')
    all_opp_tackle = cython.declare(cython.int, visibility='public')
    our_shoot = cython.declare(cython.int, visibility='public')
    opp_shoot = cython.declare(cython.int, visibility='public')
    our_dominate_time = cython.declare(cython.int, visibility='public')
    opp_dominate_time = cython.declare(cython.int, visibility='public')
    our_possession = cython.declare(cython.double, visibility='public')
    opp_possession = cython.declare(cython.double, visibility='public')
    our_kick = cython.declare(list, visibility='public')
    opp_kick = cython.declare(list, visibility='public')
    our_pass = cython.declare(list, visibility='public')
    opp_pass = cython.declare(list, visibility='public')
    pass_propability = cython.declare(list, visibility='public')
    our_through_pass = cython.declare(cython.int, visibility='public')
    opp_through_pass = cython.declare(cython.int, visibility='public')
    penalty_area = cython.declare(cython.int, visibility='public')
    our_point = cython.declare(cython.int, visibility='public')
    opp_point = cython.declare(cython.int, visibility='public')
    our_dribble = cython.declare(cython.int, visibility='public')
    opp_dribble = cython.declare(cython.int, visibility='public')
    # our_dribble_dist = cython.declare(cython.int, visibility='public')
    # opp_dribble_dist = cython.declare(cython.int, visibility='public')
    our_penalty_area = cython.declare(cython.int, visibility='public')
    opp_penalty_area = cython.declare(cython.int, visibility='public')
    our_disconnected_player = cython.declare(cython.int, visibility='public')
    opp_disconnected_player = cython.declare(cython.int, visibility='public')


    def __init__(self) -> None:
        # team_point = [ the name of target team, the name of opponent team, target team's score, opponent team's score ]
        # kick = [ left, right, front, back ]
        # pass = [ left, right, front, back ]
        # pass_probability = [ all, penalty_area, attacking_third, middle_third, defensive_third ]

        self.logname = ""
        self.target_team = "none"

        self.index = ["date",
                      "our_team",
                      "opp_team",
                      "our_final_team_point",
                      "opp_final_team_point",
                      "our_penalty_shootout_point",
                      "opp_penalty_shootout_point",
                      "final_result",  # win 3, lose 0 draw 1
                      "our_domination_time",
                      "opp_domination_time",
                      "our_possession",
                      "opp_possession",
                      "our_yellow",
                      "opp_yellow",
                      # "our_kick_all",
                      # "our_kick_L",
                      # "our_kick_R",
                      # "our_kick_F",
                      # "our_kick_B",
                      # "opp_kick_all",
                      # "opp_kick_L",
                      # "opp_kick_R",
                      # "opp_kick_F",
                      # "opp_kick_B",
                      "our_pass_all",
                      "our_pass_L",
                      "our_pass_R",
                      "our_pass_F",
                      "our_pass_B",
                      "opp_pass_all",
                      "opp_pass_L",
                      "opp_pass_R",
                      "opp_pass_F",
                      "opp_pass_B",
                      "our_through_pass",
                      "opp_through_pass",
                      "our_successed_tackle",
                      "our_failed_tackle",
                      "opp_successed_tackle",
                      "opp_failed_tackle",
                      "our_shoot",
                      "opp_shoot",
                      "our_point",
                      "opp_point",
                      "our_dribble",
                      "opp_dribble",
                      "our_penalty_area",
                      "opp_penalty_area",
                      "our_disconnected_player",
                      "opp_disconnected_player"]

        # for calculate kick_sequence
        self.kick_cycle = []
        self.kick_path_x = []
        self.kick_path_y = []
        self.all_kick_path_x = []
        self.all_kick_path_y = []
        self.color4plt_ks = []
        self.teammate_from_ball = []  # sorted from ball
        self.opponent_from_ball = []  # sorted from ball
        self.kicker = []
        self.receiver = []
        self.kick_sequence = []

        # for output
        self.team_point = ["0", "0", 0, 0, 0, 0]
        self.date = ""
        self.final_result = 0
        self.our_yellow = 0
        self.opp_yellow = 0
        self.our_tackle = 0
        self.all_our_tackle = 0
        self.opp_tackle = 0
        self.all_opp_tackle = 0
        self.our_shoot = 0
        self.opp_shoot = 0
        self.our_dominate_time = 0
        self.opp_dominate_time = 0
        self.our_possession = 0.0
        self.opp_possession = 0.0
        self.our_kick = [0, 0, 0, 0]
        self.opp_kick = [0, 0, 0, 0]
        self.our_pass = [0, 0, 0, 0]
        self.opp_pass = [0, 0, 0, 0]
        self.pass_propability = []
        self.our_through_pass = 0
        self.opp_through_pass = 0
        self.penalty_area = 0
        self.our_point = 0
        self.opp_point = 0
        self.our_dribble = 0
        self.opp_dribble = 0
        # self.our_dribble_dist = 0
        # self.opp_dribble_dist = 0
        self.our_penalty_area = 0
        self.opp_penalty_area = -1
        self.our_disconnected_player = 0
        self.opp_disconnected_player = 0

    def outputIndexForIR(self, fname: str) -> None:
        mode: str = 'a' if os.path.exists(fname) else 'w'
        f = open(fname, mode)

        csvWriter = csv.writer(f)
        csvWriter.writerow(self.index)
        f.close()

    def outputIndexForR(self, fname: str) -> None:
        mode: cython.str = 'a' if os.path.exists(fname) else 'w'
        f = open(fname, mode)

        csvWriter = csv.writer(f)
        csvWriter.writerow(self.index)
        f.close()

    def outputIntegrateResult(self, fname: str) -> None:
        mode: cython.str = 'a' if os.path.exists(fname) else 'w'
        f = open(fname, mode)

        csvWriter = csv.writer(f)

        result: list = [self.date,
                          self.team_point[0],
                          self.team_point[1],
                          self.team_point[2],
                          self.team_point[3],
                          self.team_point[4],
                          self.team_point[5],
                          self.final_result,
                          self.our_dominate_time,
                          self.opp_dominate_time,
                          self.our_possession,
                          self.opp_possession,
                          self.our_yellow,
                          self.opp_yellow,
                          # sum( self.our_kick ),
                          # self.our_kick[0],
                          # self.our_kick[1],
                          # self.our_kick[2],
                          # self.our_kick[3],
                          # sum( self.opp_kick ),
                          # self.opp_kick[0],
                          # self.opp_kick[1],
                          # self.opp_kick[2],
                          # self.opp_kick[3],
                          sum(self.our_pass),
                          self.our_pass[0],
                          self.our_pass[1],
                          self.our_pass[2],
                          self.our_pass[3],
                          sum(self.opp_pass),
                          self.opp_pass[0],
                          self.opp_pass[1],
                          self.opp_pass[2],
                          self.opp_pass[3],
                          self.our_through_pass,
                          self.opp_through_pass,
                          self.our_tackle,
                          self.all_our_tackle - self.our_tackle,
                          self.opp_tackle,
                          self.all_opp_tackle - self.opp_tackle,
                          self.our_shoot,
                          self.opp_shoot,
                          self.our_point,
                          self.opp_point,
                          self.our_dribble,
                          self.opp_dribble,
                          self.our_penalty_area,
                          self.opp_penalty_area,
                          self.our_disconnected_player,
                          self.opp_disconnected_player]

        csvWriter.writerow(result)
        f.close()

    def outputResult(self, fname) -> None:
        mode: cython.str = 'a' if os.path.exists(fname) else 'w'
        f = open(fname, mode)

        csvWriter = csv.writer(f)

        result: list = [self.date,
                        self.team_point[0],
                        self.team_point[1],
                        self.team_point[2],
                        self.team_point[3],
                        self.team_point[4],
                        self.team_point[5],
                        self.final_result,
                        self.our_dominate_time,
                        self.opp_dominate_time,
                        self.our_possession,
                        self.opp_possession,
                        self.our_yellow,
                        self.opp_yellow,
                        # sum( self.our_kick ),
                        # self.our_kick[0],
                        # self.our_kick[1],
                        # self.our_kick[2],
                        # self.our_kick[3],
                        # sum( self.opp_kick ),
                        # self.opp_kick[0],
                        # self.opp_kick[1],
                        # self.opp_kick[2],
                        # self.opp_kick[3],
                        sum(self.our_pass),
                        self.our_pass[0],
                        self.our_pass[1],
                        self.our_pass[2],
                        self.our_pass[3],
                        sum(self.opp_pass),
                        self.opp_pass[0],
                        self.opp_pass[1],
                        self.opp_pass[2],
                        self.opp_pass[3],
                        self.our_through_pass,
                        self.opp_through_pass,
                        self.our_tackle,
                        self.all_our_tackle - self.our_tackle,
                        self.opp_tackle,
                        self.all_opp_tackle - self.opp_tackle,
                        self.our_shoot,
                        self.opp_shoot,
                        self.our_point,
                        self.opp_point,
                        self.our_dribble,
                        self.opp_dribble,
                        self.our_penalty_area,
                        self.opp_penalty_area,
                        self.our_disconnected_player,
                        self.opp_disconnected_player]

        csvWriter.writerow(result)
        f.close()
