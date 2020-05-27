#! /usr/bin/env python3

import sys
import os
from pathlib import Path
import shutil




def main(args):
  # Check if ~/bin exists
  home = str(Path.home())
  bin = home + '/bin'  
  if not os.path.isdir(bin):
    os.mkdir(bin)
  
  ## Copy createCmakeProject to bin folder
  src = 'createCmakeProject.py' 
  dst = bin + '/createCmakeProject'
  try:
    shutil.copy(src, dst)
  except IOError:
    print ('Could not copy script to /bin')
    sys.exit(-1)

  print('Done, script added to ~/bin')

if __name__ == '__main__':
  main(sys.argv)