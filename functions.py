#! /usr/bin/env python3

import os

def showHelp():
    os.system('clear')
    print('\nUsage:\n')
    print(' ./play <emulator>')
    print('     - open emulator\n')
    print(' ./play <emulator> <game>')
    print('     - open game with emulator\n')
    print(' ./play show consoles')
    print('     - show consoles with available games\n')
    print(' ./play show emulators')
    print('     - show emulators available for use\n')
    print(' ./play show <console>')
    print('     - show games available from specific console')
    print('\n')
