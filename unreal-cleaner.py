# Author Łukasz Adamski
#
# Quick clean up of the Unreal Engine project
# Useful after cloning repository or migrating to a new engine version.
#

import os
import shutil

# List of directories that will be deleted
dirList = ['.vs','Binaries','Intermediate', 'Saved', 'DerivedDataCache']

# Absolute path of project
projectPath = 'D:\TheWarhorn_Workspace\TheWarhornTMP'

# If true, all files in the specified directories will be deleted
cleanPlugins = True
pluginList = ['Binaries', 'Intermediate']

#If true, recompile project after cleaning.
recompileProject = False


#Removes given directory
def removeDir(path):
    if os.path.exists(fullPath):
        shutil.rmtree(fullPath)

#Clean basic directories
for dir in dirList:
    fullPath = os.path.join(projectPath, dir)
    removeDir(fullPath)

#Clean plugins
if cleanPlugins:
    pluginsPath = os.path.join(projectPath, 'plugins')

    for path, dir, _ in os.walk(pluginsPath):
        for targetDir in pluginList:
             if targetDir in dir:
                fullPath = os.path.join(path,targetDir)
                removeDir(fullPath)
        