#! /usr/bin/env python3

import sys
import os





def main(args):
  # Check if ~/bin exists
  if os.path.isdir('~/bin'):    
    print('~/bin exists')
  else:
    print('no')


if __name__ == '__main__':
  main(sys.argv)