#This file is module of filename
#get an argument which is the name of target team
#then devide filename into target team and opponent team
#there are 4 return value [the name of target team , thename of opponent team , target team's score , opponent team's score ]


import glob #need foor getting filename

from lib import lib_log_analyzer as lib


def splitFileName( data, team ):

  a = lib.getFileName( data ).rsplit("/")[-1]

  file_name = lib.getFileName( data )

  left = str( a.split("-vs-")[0].split("-",1)[1].rsplit("_",1)[0])
  right = str( a.split("-vs-")[1].rsplit("_",1)[0])
  lpoint = a.split("-vs-")[0].rsplit("_",1)[1]
  rpoint = a.split("-vs-")[1].rsplit("_",1)[1]
  for l in open( file_name + ".rcg", 'r'):
    tmp1 = l.split();
  if(int(tmp1[1]) > 8000):
    left = a.split("-vs-")[0].split("-",1)[1].rsplit("_",2)[0]
    right = a.split("-vs-")[1].rsplit("_",2)[0]
    lpoint = a.split("-vs-")[0].rsplit("_",2)[1]
    rpoint = a.split("-vs-")[1].rsplit("_",2)[1]

  getpoint = int(lpoint)
  lostpoint = int(rpoint)

  if team == "l":
    return [left , right , getpoint , lostpoint]

  elif team == "r":
    return [right , left , lostpoint , getpoint]

  else:
    print( "emergency error : file name doesn't correspond to rcg file" )
    return ["0" , "0" , 0 , 0]
