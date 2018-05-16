#!/usr/bin/env python
import csv
from . import lib_log_analyzer as lib

class Feature:
    def __init__(self):
        # team_point = [ the name of target team, the name of opponent team, target team's score, opponent team's score ]
        # kick = [ left, right, front, back ]
        # pass = [ left, right, front, back ]
        # pass_probability = [ all, penalty_area, attacking_third, middle_third, defensive_third ]

        self.index =  [ "date",
                        "our_team",
                        "opp_team",
                        "our_final_team_point",
                        "opp_final_team_point",
                        "final_result", #win 1, lose or draw 0
                        "our_dominate_time",
                        "opp_dominate_time",
                        "our_possession",
                        "opp_possession",
                        "our_yellow",
                        "opp_yellow",
                        #"our_kick_all",
                        #"our_kick_L",
                        #"our_kick_R",
                        #"our_kick_F",
                        #"our_kick_B",
                        #"opp_kick_all",
                        #"opp_kick_L",
                        #"opp_kick_R",
                        #"opp_kick_F",
                        #"opp_kick_B",
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
                        "our_penalty_area" ]


        # for calculate
        self.target_team = "none"
        self.kick_path_x = []
        self.kick_path_y = []
        self.kick_sequence = []

        # for output
        self.team_point = [ "0", "0", 0, 0 ]
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
        self.our_kick = [ 0, 0, 0, 0 ]
        self.opp_kick = [ 0, 0, 0, 0 ]
        self.our_pass = [ 0, 0, 0, 0 ]
        self.opp_pass = [ 0, 0, 0, 0 ]
        self.pass_propability = []
        self.our_through_pass = 0
        self.opp_through_pass = 0
        self.penalty_area = 0
        self.our_point = 0
        self.opp_point = 0
        self.our_dribble = 0
        self.opp_dribble = 0
        #self.our_dribble_dist = 0
        #self.opp_dribble_dist = 0
        self.our_penalty_area = 0
        #self.opp_penalty_area = 0


    def outputIndexForIR( self, start, end ):

        fname = str(start) + "-" + str(end) + ".csv"
        f = open( fname, 'a' )

        csvWriter = csv.writer(f)
        csvWriter.writerow( self.index )
        f.close()

    def outputIndexForR(self, filename, side):

        our_team = lib.getTeamName( filename, side )
        fname = our_team + ".csv"
        f = open( fname, 'a' )

        csvWriter = csv.writer(f)
        csvWriter.writerow( self.index )
        f.close()

    def outputIntegrateResult(self, start, end):

        fname = str(start) + "-" + str(end) + ".csv"
        f = open( fname, 'a' )

        csvWriter = csv.writer(f)

        result = [ self.date,
                   self.team_point[0],
                   self.team_point[1],
                   self.team_point[2],
                   self.team_point[3],
                   self.final_result,
                   self.our_dominate_time,
                   self.opp_dominate_time,
                   self.our_possession,
                   self.opp_possession,
                   self.our_yellow,
                   self.opp_yellow,
                   #sum( self.our_kick ),
                   #self.our_kick[0],
                   #self.our_kick[1],
                   #self.our_kick[2],
                   #self.our_kick[3],
                   #sum( self.opp_kick ),
                   #self.opp_kick[0],
                   #self.opp_kick[1],
                   #self.opp_kick[2],
                   #self.opp_kick[3],
                   sum( self.our_pass ),
                   self.our_pass[0],
                   self.our_pass[1],
                   self.our_pass[2],
                   self.our_pass[3],
                   sum( self.opp_pass ),
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
                   self.our_penalty_area ]

        csvWriter.writerow( result )
        f.close()


    def outputResult(self, filename, side):

        our_team = lib.getTeamName( filename, side )
        fname = our_team + ".csv"
        f = open( fname, 'a' )

        csvWriter = csv.writer(f)

        result = [ self.date,
                   self.team_point[0],
                   self.team_point[1],
                   self.team_point[2],
                   self.team_point[3],
                   self.final_result,
                   self.our_dominate_time,
                   self.opp_dominate_time,
                   self.our_possession,
                   self.opp_possession,
                   self.our_yellow,
                   self.opp_yellow,
                   #sum( self.our_kick ),
                   #self.our_kick[0],
                   #self.our_kick[1],
                   #self.our_kick[2],
                   #self.our_kick[3],
                   #sum( self.opp_kick ),
                   #self.opp_kick[0],
                   #self.opp_kick[1],
                   #self.opp_kick[2],
                   #self.opp_kick[3],
                   sum( self.our_pass ),
                   self.our_pass[0],
                   self.our_pass[1],
                   self.our_pass[2],
                   self.our_pass[3],
                   sum( self.opp_pass ),
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
                   self.our_penalty_area ]

        csvWriter.writerow( result )
        f.close()



class Team:
    def __init__(self, teamname):
        self.name = teamname
        self.player = []
        for i in range( 11 ):
            self.player.append( Player() )
        self.offsideLineX = 0.0


class Player:
    def __init__(self):
        self.hetero = -1
        self.state = "0x1"
        self.pos = Position()
        self.vel = Position()
        self.body_angle = 0.0
        self.neck_angle = 0.0
        self.view_area = 0
        self.stamina = 8000
        self.stamina_capacity = 130600
        self.action = ""

class Position:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Ball:
    def __init__(self):
        self.pos = Position()
        self.vel = Position()

class Referee:
    def __init__(self):
        self.playmode = ""
        self.say = []
        self.said = False

class ServerParam:
    def __init__(self):
        self.pitch_length = 105.0
        self.pitch_width = 68.0
        self.goal_line_l = -52.5
        self.goal_line_r = 52.5
        self.goal_post = 7
        self.penalty_area_x = 36.05
        self.penalty_area_y = 20.00
        self.ball_speed_decay = 0.94
        self.hetero = []
        for i in range( 18 ):
            self.hetero.append( HeteroParam() )


class HeteroParam:
    def __init__(self):
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


class WorldModel:

    def __init__(self, team_l, team_r):
        self.ball = Ball()
        self.l = Team( team_l )
        self.r = Team( team_r )
        self.referee = Referee()
        self.dominate_side = "none"
        self.last_kicker_unum = -1
        self.last_kicked_cycle = -1
