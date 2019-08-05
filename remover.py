#
#It's so simple... very straightforward!
#
#Trina S.
#

import os

#Put the initial folder you would like to remove "._" files.
DIR='./images'

for path, subdirs,files in os.walk(DIR):
  for name in files:
    #print(name) name is only file name, no path included.
    #TEST=name[:2]
    #print(TEST)
    #Let's put eveything together!--> for os.remove()
    FilePath=os.path.join(os.getcwd(), path[2:], name)
    print(FilePath)
    if name[:2] == '._':
      os.remove(FilePath)
      print("Deleted!")


