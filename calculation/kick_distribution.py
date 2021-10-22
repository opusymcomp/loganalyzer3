#!/usr/bin/env python
# cython: language_level=3
# -*- coding: utf-8 -*-

import cython

from lib import lib_log_analyzer as lib
from lib import la_class


def saveKickDistribution( feat: la_class.Feature, path: str, degree_range: cython.int = 90 ) -> None:

    with open( path+'kick_distribution.csv', 'a' ) as f:

        file_pointers: list = []
        for i in range(-180, 180, degree_range):
            fp = open("kick_distribution_{}_{}.csv".format(i, i+degree_range), "a")
            file_pointers.append(fp)
        f_success = open("kick_distribution_success.csv", "a")

        for i in range( len( feat.kick_sequence ) - 1 ):
            degree: cython.int = lib.changeRadianToDegree(lib.calcRadianC(feat.kick_sequence[i][1], feat.kick_sequence[i][2],
                                                                          feat.kick_sequence[i + 1][1],
                                                                          feat.kick_sequence[i + 1][2]))

            # if not terminal condition
            if ( feat.kick_sequence[i][4] != -1 \
                 and feat.kick_sequence[i+1][4] != 0 ):
                f.write( str( feat.kick_sequence[i][1] ) + ',' +
                         str( feat.kick_sequence[i][2] ) + ',' +
                         str( lib.calcDistC( feat.kick_sequence[i][1],
                                             feat.kick_sequence[i][2],
                                             feat.kick_sequence[i+1][1],
                                             feat.kick_sequence[i+1][2] ) ) + ',' +
                         str(degree) +
                         str('\n') )

                if (feat.kick_sequence[i][3] == 1):
                    f_success.write( str( feat.kick_sequence[i][1] ) + ',' +
                             str( feat.kick_sequence[i][2] ) + ',' +
                             str( lib.calcDistC( feat.kick_sequence[i][1],
                                                 feat.kick_sequence[i][2],
                                                 feat.kick_sequence[i+1][1],
                                                 feat.kick_sequence[i+1][2] ) ) + ',' +
                             str(degree) +
                             str('\n') )

                fp_ind = int((degree + 180) / degree_range)

                file_pointers[fp_ind].write( str( feat.kick_sequence[i][1] ) + ',' +
                                             str( feat.kick_sequence[i][2] ) + ',' +
                                             str( lib.calcDistC( feat.kick_sequence[i][1],
                                                                 feat.kick_sequence[i][2],
                                                                 feat.kick_sequence[i+1][1],
                                                                 feat.kick_sequence[i+1][2] ) ) + ',' +
                                             str(degree) +
                                             str('\n') )

        for fp in file_pointers:
            fp.close()
        f_success.close()


def printKickDistribution( sp: la_class.ServerParam, feat: la_class.Feature, path: str ) -> None:

    import matplotlib
    #matplotlib.use('Agg')
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.patches import Circle
    import mpl_toolkits.mplot3d.art3d as art3d
    from matplotlib import pyplot as plt
    import matplotlib.font_manager as fm

    xlim: cython.double = sp.pitch_length / 2 + 5.0
    ylim: cython.double = sp.pitch_width / 2 + 5.0
    fm._rebuild()
    #plt.rc('font', family='Times New Roman')
    #plt.rcParams['font.family'] = 'Times New Roman'

    fig = plt.figure(figsize=(10.5, 6.8))
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    ax = fig.add_subplot( 111, projection='3d', azim = 240 )

    ax.set_xlabel("{\it x}", fontsize=32, labelpad=20)
    ax.set_ylabel("{\it y}", fontsize=32, labelpad=20)
    ax.set_zlabel("{\it distance}", fontsize=32, labelpad=20)

    ax.set_xlim( -xlim, xlim )
    ax.set_ylim( ylim, -ylim )

    ax.tick_params(labelsize=32, pad=10)

    # plot soccer fields
    ax.plot3D( [ sp.goal_line_l, -sp.penalty_area_x ], [ -sp.penalty_area_y, -sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_l, -sp.penalty_area_x ], [ sp.penalty_area_y, sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_r, sp.penalty_area_x ], [ -sp.penalty_area_y, -sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_r, sp.penalty_area_x ], [ sp.penalty_area_y, sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ -sp.penalty_area_x, -sp.penalty_area_x ], [ sp.penalty_area_y, -sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.penalty_area_x, sp.penalty_area_x ], [ sp.penalty_area_y, -sp.penalty_area_y ],[ 0, 0 ], color='g', linewidth=4 )

    ax.plot3D( [ sp.goal_line_l, sp.goal_line_r ], [ -sp.pitch_width / 2, -sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_l, sp.goal_line_r ], [ sp.pitch_width / 2, sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_l, sp.goal_line_l ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_r, sp.goal_line_r ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )

    plt.plot( [ 0, 0 ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], color='g', linewidth=4 )

    p = Circle((0.5, 0.5), 9, ec="g", fc="None", linewidth=4 )
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0.0, zdir="z")

    # plot kick distribution
    for i in range( len( feat.kick_sequence ) - 1 ):
        # if not tarminal condition
        if ( feat.kick_sequence[i][4] != -1 \
             and feat.kick_sequence[i+1][4] != 0 ):
            ax.plot3D( [ feat.kick_sequence[i][1], feat.kick_sequence[i][1] ],
                       [ feat.kick_sequence[i][2], feat.kick_sequence[i][2] ],
                       [ 0,  lib.calcDistC( feat.kick_sequence[i][1],
                                            feat.kick_sequence[i][2],
                                            feat.kick_sequence[i+1][1],
                                            feat.kick_sequence[i+1][2] ) ],
                       "red" )

    filename: cython.str = path + feat.team_point[0] + "-kick_distribution"
    extension: list = [".eps", ".pdf", ".png", ".svg"]
    for e in extension:
        plt.savefig(filename+e, dpi=300, bbox_inches="tight", transparent=True)
    plt.show()
