#! /usr/bin/env python3

import os
import sys
import shutil



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
    cmakeFile.write('cmake_minimum_required(VERSION {})\n'.format('3.1'))
    cmakeFile.write('\n')
    cmakeFile.write('project({})'.format(projectName))
    cmakeFile.write('\n')
    cmakeFile.write('\n')
    cmakeFile.write('if(EXISTS {})\n'.format('${PROJECT_SOURCE_DIR}/testing'))
    cmakeFile.write('\tmessage(STATUS "Including /testing directory")\n')
    cmakeFile.write('\tadd_subdirectory({})\n'.format('${PROJECT_SOURCE_DIR}/testing'))
    cmakeFile.write('endif(EXISTS {})\n'.format('${PROJECT_SOURCE_DIR}/testing'))



def createBasicMain(directory):
  mainFile = directory + '/main.cpp'
  os.mknod(mainFile)

  with open(mainFile, 'a') as main:
    main.write('#include <iostream>\n')
    main.write('\n')
    main.write('\n')
    main.write('using std::cout;\n')
    main.write('using std::cerr;\n')
    main.write('using std::endl;\n')
    main.write('using std::string;\n')
    main.write('\n')
    main.write('\n')
    main.write('\n')
    main.write('int main(int argc, char **argv) {\n')
    main.write('\n')
    main.write('\n')
    main.write('\tcout << "Hello, world!" << endl;\n')
    main.write('\n')
    main.write('\n')
    main.write('\treturn EXIT_SUCCESS;\n')
    main.write('\n')
    main.write('}\n')

def createBasicCMakeLists(directory):
  cmakeFile = directory + '/CMakeLists.txt'
  os.mknod(cmakeFile)

  with open(cmakeFile, 'a') as cmake:
    cmake.write('\n')
    cmake.write('\n')
    cmake.write('add_executable(main main.cpp)\n')
    cmake.write('\n')

def createTestingFolder(testingDir):
  # Create a basic main.cpp
  createBasicMain(testingDir)

  # Create a testing/CMakeLists
  createBasicCMakeLists(testingDir)

def setupVsCode(folderPath):
  # Create .vscode folder
  vscodeFolder = folderPath + '/.vscode'
  os.mkdir(vscodeFolder)

  # Create .vscode/settings.json
  settingsFile = vscodeFolder + '/settings.json'
  os.mknod(settingsFile)

  # Add the autosave to vscodeFile
  with open(settingsFile, 'a') as settings:
    settings.write('{\n')
    settings.write('\t"files.autoSave": "onFocusChange"\n')
    settings.write('}\n')

def createFolderStructure(folderPath):
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
  createMainCMakeLists(folderPath)
  # Testing folder
  createTestingFolder(testingDir)

  # Add .vscode settings (autosave)
  setupVsCode(folderPath)



def main():

  useForce = False

  args = sys.argv
  if len(args) < 2:
    print('Please five a folderName as argument')
    sys.exit(-1)

  if ('--force' in args or '-f' in args):
    useForce = True

  folderPath = args[1]  
  ## If doesn't exist, create folder
  if not doesFolderExist(folderPath):
    createFolderStructure(folderPath)
  else:
    if (useForce):
      print('Deleting folder')
      shutil.rmtree(folderPath)
      print('Creating folder')
      createFolderStructure(folderPath)
    else:
      print('Folder exists!')

  print('Done')

if __name__ == '__main__': 
  main()