import math
import sys

from lib import lib_log_analyzer as lib

def KickTxt( data, date ):

  if( len(data) == 3 ):
    a = data[1].split( ".r" )[0]
    team = data[2].split( "-" )[1]

  x = [];
  y = [];
  x_tmp = [];
  y_tmp = [];
  x_kick = [];
  y_kick = [];
  x_pass = [];
  y_pass = [];
  time = [];
  player = [];
  kick_player = [];
  pass_player = [];
  lines = [];

  left = a.split( "-vs-" )[0].split( "-", 1 )[1].rsplit( "_", 1 )[0]
  right = a.split( "-vs-" )[1].rsplit( "_", 1 )[0]
  cycle = '0'

  for l in open( a + ".rcg", 'r' ):

    if ( "show" in l ):

      tmp = l.split();

      if( cycle != tmp[1] ):

        x.append( float( tmp[3] ) )
        y.append( float( tmp[4] ) )

        if( len( x ) == 2999 ):

          x.append( float( tmp[3] ) )
          y.append( float( tmp[4] ) )
          lines.append( l )

        cycle = tmp[1]
        lines.append( l )


  for m in open( a + ".rcl", 'r' ):

    if( "(kick" in m ):

      tmp = m.split();
      logcycle = tmp[0].split( ',' )
      time.append( int( logcycle[0] ) )
      logteam = tmp[2].split( '_' )

      while( len( logteam ) > 2 ):

        logteam[0] = logteam[0] + "_" + logteam[1]
        logteam.pop( 1 )

      if( logteam[0] == left ):

        logteam[0] = 'l'

      else:

        logteam[0] = 'r'

      if( logteam[1] == '10:' or logteam[1] == '11:' ):

        logteam[1] = logteam[1][0] + logteam[1][1]

      else:

        logteam[1] = logteam[1][0]

      player.append( logteam )



  for i in range( len( time ) ):

    tmp = lines[time[i]-1].split()

    for j in range( len( tmp )-1 ):

      if( tmp[j] == '(('+player[i][0] and tmp[j+1] == player[i][1]+')' ):

        x_tmp.append( float( tmp[j+4] ) )
        y_tmp.append( float( tmp[j+5] ) )

        if( math.sqrt( ( x_tmp[i] - x[time[i]-1] ) ** 2 + ( y_tmp[i] - y[time[i]-1] ) ** 2 ) < 1.5 ):

          x_kick.append( x[time[i]-1] )
          y_kick.append( y[time[i]-1] )
          kick_player.append( player[i] )


  f = open( date + '_kick_dist.txt', 'a' )


  for i in range( len( x_kick )-1 ):

    if( kick_player[i][0] == kick_player[i+1][0] and kick_player[i][0] == team ):

      dist = math.sqrt( ( x_kick[i] - x_kick[i+1] ) ** 2 + ( y_kick[i] - y_kick[i+1] ) ** 2 )

      if( kick_player[i][0] == "l" ):

        f.write( str( x_kick[i] )+" "+str( y_kick[i] )+" "+str( dist )+'\n' )

      elif( kick_player[i][0] == "r" ):

        f.write( str( -x_kick[i] )+" "+str( -y_kick[i] )+" "+str( dist )+'\n' )

  f.close()
