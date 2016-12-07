#! /usr/bin/env python3

import os
import sys

# used in play.py

def showHelp():
    os.system('clear')
    print('\nUsage:\n')
    print(' play <emulator>')
    print('     - open emulator\n')
    print(' play <emulator> <game>')
    print('     - open game with emulator\n')
    print(' play show consoles')
    print('     - show consoles with available games\n')
    print(' play show emulators')
    print('     - show emulators available for use\n')
    print(' play show <console>')
    print('     - show games available from specific console')
    print('\n')






# used in both replace.py and romcleaner.py

def getConsolesPath():
    ''' try to change directory to rom folder on flash drive '''

    try:
        os.chdir('/Volumes/UBUNTU 16_0/retropie/roms/')
        consolesPath = 'Volumes/UBUNTU 16_0/retropie/roms/'
    except:
        print('\nCould not find USB. Using local game directory.\n')
        home = os.path.expanduser('~')
        consolesPath = '{home}/Games/roms/'.format(
            home=home
        )
    return consolesPath

def getConsoleFromUser(consoleList):
    ''' ask user which console folder they want to clean up '''
    console = input('Which consoles folder do you want to clean up?\n').lower()
    while not (console in consoleList):
        print('\n{console} isn\'t found.\n'.format(
            console=console.title()
        ))
        console = input('Which consoles folder do you want to clean up?\n').lower()
    return console






# used in replace.py

def rename(folderName):
    print('\nThis folder\'s name is {folderName}. Would you like to rename it? (y/N)'.format(
        folderName=folderName))

    answer = input()

    if answer.lower() == 'quit':
        print('Saving changes and quitting.\n')
        sys.exit(0)

    while answer != 'y' and answer != 'N':
        print('\nNot understood. Would you like to rename {folderName}?\n'.format(
            folderName=folderName))
        answer = input()

    if answer == 'N':
        return 'skip'
    elif answer == 'y':
        newFolderName = input('\n{folderName} will be renamed what?\n'.format(
            folderName=folderName))
        return newFolderName

def verifyRename(newFolderName):
    print('\nYou chose {newFolderName}. Is this correct? (y/N)'.format(
        newFolderName=newFolderName
        ))
    answer = input()
    return answer
