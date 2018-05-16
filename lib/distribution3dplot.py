from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import sys
import numpy as np

def Plot3d( date ):

  x = []
  y = []
  z = []

  fig = plt.figure()
  ax = Axes3D( fig )
  txtname = date + '_kick_dist.txt'

  for l in open( txtname, 'r' ):
    tmp = l.split();
    ax.plot3D( [float( tmp[0] ), float( tmp[0] )], [float( tmp[1] ), float( tmp[1] )], [0, float( tmp[2] )], "red" )
    x.append( float( tmp[0] ) )
    y.append( float( tmp[1] ) )
    z.append( float( tmp[2] ) )

  ax.plot3D( [0,0], [34,-34], [0,0], 'g' )
  ax.plot3D( [52.5,52.5], [34,-34], [0,0], 'g' )
  ax.plot3D( [-52.5,-52.5], [34,-34], [0,0], 'g' )
  ax.plot3D( [52.5,-52.5], [34,34], [0,0], 'g' )
  ax.plot3D( [52.5,-52.5], [-34,-34], [0,0], 'g' )
  ax.plot3D( [-36,-36], [20.16,-20.16], [0,0], 'g' )
  ax.plot3D( [36,36], [20.16,-20.16], [0,0], 'g' )
  ax.plot3D( [52.5,36], [20.16,20.16], [0,0], 'g' )
  ax.plot3D( [52.5,36], [-20.16,-20.16], [0,0], 'g' )
  ax.plot3D( [-52.5,-36], [20.16,20.16], [0,0], 'g' )
  ax.plot3D( [-52.5,-36], [-20.16,-20.16], [0,0], 'g' )

  fig.suptitle( 'Kick_distribution' )
  fig.savefig( date + '.png' )
