#! /usr/bin/env python3

import os
import sys



def doesFolderExist(folderName):
  if os.path.isdir(folderName):
    return True
  return False

def createMainCMakeLists(folderName):

  projectName = 'projectName'

  ## Create file
  filePath = folderName + '/CMakeLists.txt'
  os.mknod(filePath)

  # Open file to write to it
  with open(filePath, 'a') as cmakeFile:
    cmakeFile.write('cmake_minimum_version(VERSION {})\n'.format('3.1'))
    cmakeFile.write('\n')
    cmakeFile.write('project({})'.format(projectName))
    cmakeFile.write('\n')
    





def main():
  args = sys.argv
  if len(args) != 2:
    print('Please five a folderName as argument')
    sys.exit(-1)

  folderPath = args[1]  
  ## If doesn't exist, create folder
  if not doesFolderExist(folderPath):
    os.mkdir(folderPath)
    #print('Created folder: {}'.format(folderPath))

    ## Also create each subfolder src, include, tests, testing, examples, tools
    srcDir = folderPath + '/src'
    includeDir = folderPath  + '/include'
    testsDir = folderPath + '/tests'
    testingDir = folderPath + '/testing'
    examplesDir = folderPath + '/examples'
    toolsDir = folderPath + '/tools'

    # If something fails, clean up
    try:
      os.mkdir(srcDir)
      os.mkdir(includeDir)
      os.mkdir(testsDir)
      os.mkdir(testingDir)
      os.mkdir(examplesDir)
      os.mkdir(toolsDir)
    except:      
      print('An exception occured in sub-directory creating... Cleaning up and exiting...')
      ## Actually cleanup

      sys.exit(-1)


    ## Create all files

    # Main CMakeLists
    createMainCMakeLists(folderPath);







    print('Done')


  
    



if __name__ == '__main__': 
  main()