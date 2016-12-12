#! /usr/bin/env python3

# TODO: if changing functionality to replace /console with /console_cleaned,
#     first make console get replaced with console_cleaned
#     the ctrl + f 'console with cleaned' and change those lines

'''''''''''''''''''''''''''''''''''''''''''''
#                DOC HAIKU                  #
#          typing stuff is dumb             #
#       run this here program instead       #
#         save yer fingerstrength           #
#                                           #
'''''''''''''''''''''''''''''''''''''''''''''


import os
import sys
from data import *
from functions import *

# initialize directories to be used by play.py
home = os.path.expanduser('~')
emulators = os.listdir('{home}/Games/emulators/'.format(home=home))
systems = os.listdir('{home}/Games/roms/'.format(home=home))
consolesPath = '{home}/Games/roms/'.format(home=home)

# OpenEmu does not emulate the user-specified console
openEmuFlag = False




    # if user is specifying a game via OpenEmu
    # this was a late addition so it's gross and messy
    if len(sys.argv) == 4:
        if (sys.argv[1] == 'openemu') and (sys.argv[2] in consoleDict.keys()) and (sys.argv[3].lower() in os.listdir(consolesPath + '{system}_cleaned/'.format(
                system=sys.argv[2].lower()))):  # change this line if replace with cleaned

            # system = 'nes'
            system = sys.argv[2].lower() + '_cleaned'  # change this line if replace with cleaned
            # game = 'contra'
            game = sys.argv[3].lower()
            # extension = ''
            extension = ''


            if system[:len(system) - len('_cleaned')] in extensionDict.keys():  # change this line if replace with cleaned
                for ext in extensionDict[system[:len(system) - len('_cleaned')]]:  # change this line if replace with cleaned
                    for i in os.listdir(consolesPath + '{system}/{game}'.format(  # change this line if replace with cleaned
                        system=system,
                        game=game)):
                        if i.endswith(ext):
                            extension = ext
                            command = 'open -a OpenEmu {systems}{system}/{game}/{game}{ext}'.format(
                                systems=consolesPath,
                                system=system,
                                game=game,
                                ext=extension)
                            os.system(command)
                            sys.exit(0)
    showHelp()
    sys.exit(0)




'''                                 PART I
                                help, or show





    PLAY SHOW'''

# user is asking to see something
if sys.argv[1].lower() == 'show':

    ''' find out what the user wants to be shown and show it '''

    # if user only says 'show'
    if len(sys.argv) == 2:
        showHelp()
        sys.exit(0)

    # this is what user is asking to be shown
    system = sys.argv[2].lower()

    # collect console if exists
    for key, value in consoleDict.items():
        if system in value:
            system = key
            continue

    # show games if user asks
    if system in systems:
        os.system('clear')
        print('\nHere are the games available for {system}:\n'.format(
            system=system))
        for game in os.listdir('{home}/Games/roms/{system}_cleaned/'.format(  # change this when console with cleaned
            home=home,
            system=system)):
            print(game.lower())

    # show consoles if user asks
    elif system == 'consoles' or sys.argv[2].lower() == 'systems':
        os.system('clear')
        print('\nHere are the consoles with games available:\n')
        for console in os.listdir('{home}/Games/roms/'.format(
            home=home)):
            print(console.lower())

    # show emulators if user asks
    elif system == 'emulators':
        os.system('clear')
        print('\nHere are the emulators available for use:\n')
        for emu in os.listdir('/Users/davidmaness/Games/emulators/'):
            print(emu.lower())

    print('\n')
    sys.exit(0)


''' PLAY HELP '''

# if user is asking for help
if sys.argv[1].lower() == 'help' or sys.argv[1].lower() == 'use' or sys.argv[1].lower() == 'usage':
    showHelp()
    sys.exit(0)

# if first argument isn't show or help, assign it to system
system = sys.argv[1].lower()









'''                                           PART II
                                 user is asking to open a program





              /----yes---- (consoleExists==True, emulatorExists==False, system == <console>, emulator == <emulator>)
 console? ---/
              \                           /-----yes (consoleExists==False, emulatorExists==True, system == <emulator>)
               \----no--- emulator? -----/
                                          \
                                           \----no---- error -> quit
'''


# find out if user provided a console or an emulator
isConsole, isEmulator = False, False

# check all consoles
for key, value in consoleDict.items():
    if system in value:
        system = key
        # check emulators for console
        for key, value in emulatorConsoleDict.items():
            if system in value:
                emulator = key
        isConsole = True

# if not a console, check all emulators
if not isConsole:
    for key, value in emulatorConsoleDict.items():
        if system == key.lower():
            system = key.lower()
            isEmulator = True

    # if not a console or an emulator, return an error and quit
    if not isEmulator:
        print('Console or emulator \'{system}\' not understood.'.format(
            system=system))
        sys.exit(1)


# now the program knows whether to launch a console or emulator
# and the exact console or emulator is stored in system

if isConsole:
    if system in openEmuList:
        command = 'open -a OpenEmu'
    else:
        if emulator in wineList:
            command = 'wine ~/Games/emulators/{emulator}/{emulator}.exe'.format(
                emulator=emulator
                )
        elif emulator in osxList:
            command = 'open -a {emulator}'


elif isEmulator:
    if system in wineList:
        command = 'wine ~/Games/emulators/{system}/{system}.exe'.format(
            system=system)
    elif system in osxList:
        command = 'open -a {system}'.format(
            system=system)
else:
    print('There has been an error.\nSystem check is leaking.')
    sys.exit(2)





'''                                 PART III
                       if user asks to open a specific game
'''



# run this only if a second argument (game) is specified
if len(sys.argv) == 3:


    # figure out the game user wants to play

    game = sys.argv[2].lower()
    # create game filepath from user input
    gamePath = '{home}/Games/roms/{system}_cleaned/{game}/'.format(  # change this line if replace with cleaned
        home=home,
        system=system,
        game=game)


    # if the game doesn't exist, throw an error

    if not os.path.isdir(gamePath):
        print('\nCannot find the game {game}.\nIt\'s possible the game folders have not been renamed.\n'.format(
            game=game))
        sys.exit(1)

    # find the extension for parsing the games directory

    extension = 'NULL'
    print(gamePath)

    for i in os.listdir(gamePath):
        print(i)
        for ext in extensionDict[system]:
            # this part will only work if game files
            # have the same name as their containing folder
            if i == '{game}{ext}'.format(game=game, ext=ext):
                extension = ext
                continue

    if extension == 'NULL':
        print('\nCannot find the game {game}.\nIt\'s possible the filename has not yet been formatted.\n'.format(
            game=game))
        sys.exit(1)


    # add game filepath to the command
    command += ' ' + gamePath + '{game}{ext}'.format(
        home=home,
        system=system,
        game=game,
        ext=extension)


# next line is for debugging
print('Command: {command}'.format(command=command))


# run command and play!
os.system(command)

# exit program
sys.exit(0)
