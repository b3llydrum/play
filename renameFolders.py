#! /usr/bin/env python3


'''''''''''''''''''''''''''''''''''''''''''''
#                DOC HAIKU                  #
#          your folders look gross          #
#        let me help you rename them        #
#            isn't that better?             #
#                                           #
'''''''''''''''''''''''''''''''''''''''''''''

# run from inside console folder


import os
import sys
from pprint import pprint
from functions import *

# go to where the consoles live
homeDir = os.path.expanduser('~')
consolesPath = getConsolesPath()
os.chdir(consolesPath)

# create list of known consoles
consoleList = [system for system in os.listdir(consolesPath) if os.path.isdir(system)]

# print out consoles for user to choose from
for console in consoleList:
    if 'cleaned' not in console and 'working' not in console:
        print(console)
print('\n')

# ask user which console folder they want to clean up
console = getConsoleFromUser(consoleList)


# create list of game folder names for user to clean
gameList = os.listdir(consolesPath + '/' + console)

pprint(gameList)
print('\n')

startingGameIndex = 0

# ask if user wants to skip to a game
skipCheck = input('Do you want to skip to a specific game folder? (y/N)\n')
while skipCheck != 'y' and skipCheck != 'N':
    skipCheck = input('Not understood. Do you want to skip to a game folder in the directory? (y/N)\n')
if skipCheck == 'y':
    for i in gameList:
        print(i)
    print('\n')
    startingGame = input('Which game would you like to start with?\n')
    while startingGame not in gameList:
        startingGame = input('{game} is not in current folder. Which game would you like to start with?\n'.format(
            game=startingGame)).lower()
    startingGameIndex = gameList.index(startingGame)

print('Starting at {firstGameFolder}.'.format(firstGameFolder=gameList[startingGameIndex]))



# loop through the folder names
for i in range(startingGameIndex, len(gameList)):
    # special folders start with '0X - '
    if gameList[i][0] != '0' and not os.path.isdir(gameList[i]):

        gameFolderPath = '{consolesPath}{console}/'.format(
            consolesPath=consolesPath,
            console=console)

        # get new folder name from user
        newFolderName = rename(gameList[i])

        if newFolderName == 'skip':
            continue

        # verify that the new name is correct
        answer = verifyRename(newFolderName)
        while answer != 'y':
            newFolderName = rename(gameList[i])
            answer = verifyRename(newFolderName)

        print('\n{folderName} is now {newFolderName}!'.format(
            folderName=gameList[i],
            newFolderName=newFolderName))

        # do one of two things depending on if the renamed folder is the same or not

        # if the renamed folder is the same as the original name
        if gameList[i].lower() == newFolderName.lower():

            # create temporary copy folder with different name
            os.system('sudo cp -R {gameFolderPath}{folderName}/ {gameFolderPath}new_{folderName}'.format(
                gameFolderPath=gameFolderPath,
                folderName=gameList[i]))

            # remove the original folder
            os.system('sudo rm -rf {gameFolderPath}{folderName}'.format(
                gameFolderPath=gameFolderPath,
                folderName=gameList[i]))

            # copy different named folder into final folder
            os.system('sudo cp -R {gameFolderPath}new_{folderName}/ {gameFolderPath}{newFolderName}'.format(
                gameFolderPath=gameFolderPath,
                folderName=gameList[i], newFolderName=newFolderName))

            # remove temporary copy folder
            os.system('sudo rm -rf {gameFolderPath}new_{folderName}'.format(
                gameFolderPath=gameFolderPath,
                folderName=gameList[i]))
        else:
            os.system('sudo cp -R {gameFolderPath}\"{folderName}\"/ {gameFolderPath}{newFolderName}'.format(
                gameFolderPath=gameFolderPath,
                folderName=gameList[i],
                newFolderName=newFolderName))
            os.system('sudo rm -rf {gameFolderPath}\"{folderName}\"'.format(
                gameFolderPath=gameFolderPath,
                folderName=gameList[i]))

print('\nAll done!\n')
sys.exit(0)
