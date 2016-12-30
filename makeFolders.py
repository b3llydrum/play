#! /usr/bin/env python3


'''''''''''''''''''''''''''''''''''''''''''''
#                DOC HAIKU                  #
#           got a ton o' games?             #
#       run this bad boy and then run       #
#              renameFiles.py               #
#                                           #
'''''''''''''''''''''''''''''''''''''''''''''

# TODO: make stopCopyingIndex depend on console extension

import os
import sys
from data import *
from functions import *
from pprint import pprint



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

# go to the folder with all the console folders
os.chdir(consolesPath)


# create list of game folder names for user to clean
gameList = os.listdir(console)
actualGameList = []
# late addition... too late... only add files not folders
for i in gameList:
    if os.path.isdir(console + '/' + i):
        pass
    else:
        actualGameList.append(i)
gameList = actualGameList

def firstClean(gameList):  # Ratatouille (E)(Puppa).gba
    newGameList = []
    for title in gameList:
        newTitle = ''
        # this index stops the for loop from copying the extension
        stopCopyingIndex = -3  # TODO: make this depend on console extension
        # this for loop removes unwanted characters
        for i in range(len(title)):
            if title[i] not in skippableChars:
                newTitle += title[i]
            if i < len(title) - 1:
                if title[i] + title[i + 1] == ' (':
                    stopCopyingIndex = i
        # this next line lowers case and removes spaces
        newGameList.append('_'.join(newTitle[:stopCopyingIndex].lower().split()))
    return newGameList

def secondClean(newGameList): # ratatouille_(e)(puppa)
    gameList = []
    cleanedGameList = []
    for title in newGameList:
        newTitle = ''
        for i in range(len(title)):
            if i < len(title) - 2:

                if title[i] + title[i + 1] == '__':   # removes double underscores
                    continue

                if title[i] + title[i + 1] + title[i + 2] == '_-_':
                    continue
                elif title[i - 1] + title[i] + title[i + 1] == '_-_':
                    continue
                else:
                    newTitle += title[i]

            else:
                if title[i - 1] + title[i] == '__':
                    continue
                else:
                    newTitle += title[i]

        gameList.append(newTitle)
    for title in gameList:
        if title[:4] == 'the_':
            cleanedGameList.append(title[4:])
        else:
            cleanedGameList.append(title)

    return cleanedGameList


# do all the cleaning defined above and print the first 100 results
newGameList = firstClean(gameList)
newGameList = secondClean(newGameList)


for i in range(len(gameList)):
    cleanedName = newGameList[i]
    if newGameList[i].endswith('_the'):
        print(newGameList[i] + ' ends with _the')
        cleanedName = newGameList[i][:-4]
    # if not already a folder
    if not os.path.isdir('{console}/{folder}'.format(
        console=console,
        folder=cleanedName)):
        # then MAKE folder
        os.system('sudo mkdir {console}/{folder}'.format(
            console=console,
            folder=cleanedName))
    # move the game into the new folder
    os.system('sudo mv {console}/"{game}" {console}/{folder}'.format(
        console=console,
        game=gameList[i],
        folder=cleanedName))
    print('Moved    "{game}"    into    {folder}'.format(
        game=gameList[i],
        folder=cleanedName))
