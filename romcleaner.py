#! /usr/bin/env python3


'''''''''''''''''''''''''''''''''''''''''''''
#                DOC HAIKU                  #
#         provides some simple help         #
#         by renaming all your roms         #
#            with consistency               #
#                                           #
'''''''''''''''''''''''''''''''''''''''''''''

# LOGIC FLOW
# create destination folders for each flag
# check filename for patterns
# flip flags to True if patterns fit
# create folder for game based on original folder name inside each flag folder
# copy file into each flag folder
# once done with every file, rename each file in each folder according to flag
# if in this folder and in this folder, etc etc etc
#   prioritize pure files and put back into snes_cleaned folder
#   then put all region files that arent also in tag or beta
#   if no files still, put region files that are in tag


import re
import os
import shutil
import sys
import time
from data import *
from functions import *



# ~/Games/roms/
consolesPath = getConsolesPath()


# every console folder in consolesPath
consoleList = [system for system in os.listdir(consolesPath)]


# print every console for user to choose from
for console in consoleList:
    print(console)
print('\n')



# ask user which console folder they want to clean up
console = getConsoleFromUser(consoleList)


# change directory to the parent of console
os.chdir(consolesPath)



''' once console folder is chosen,
        create backup folder on which to operate
            and create new folder to paste everything into  '''


# create backup folder for uncleaned console folder


# 1. remove {console}_working/
# 2. add empty {console}_working/
# 3. remove {console}_cleaned/
# 4. add new {console}_cleaned/
# 5. switch to {console}_working/

# first delete any existing backup folder
if os.path.exists(console + '_working'):
    print('\nDeleting current {console}_working/ folder...'.format(console=console))
    os.system('sudo rm -rf ' + console + '_working')


# then copy console folder into backup folder
os.makedirs(console + '_working')
print('Creating new {console}_working/ folder...'.format(console=console))
os.system('sudo cp -R ' + console + '/ ' + console + '_working')


# create destination folder
if os.path.exists(console + '_cleaned'):
    print('\nDeleting current {console}_cleaned/ folder...'.format(console=console))
    os.system('sudo rm -rf ' + console + '_cleaned')
print('... and creating new {console}_cleaned/ folder as destination.\n'.format(console=console))
os.makedirs(console + '_cleaned')
time.sleep(1)


# switch to backup console folder
os.chdir(console + '_working')
print('Moved to {console}_working/ folder to do operations.'.format(console=console))
time.sleep(2)


# and at the end, replace the original console folder with the _cleaned folder








'''               ^
                 / \
                  |
                  |
                  |-------   that stuff made the working and cleaned folders





                  |------   this stuff does the following:
                  |               - tags each file
                  |               - sorts them into their own tag folders
                  |               -
                 \ /
                  v





'''


buffer_file = ''

regions = ['U', 'J', 'E', 'G', 'F']

extension = []

for key, value in extensionDict.items():
    if key == console:
        for ext in value:
            extension.append(ext[1:])
extension = '|'.join(extension)

# create regex object to match filenames with no tags
# Sim Ant.smc
purePattern = re.compile(r'[^\]][^\)]\.({extension})'.format(extension=extension))


# create regex object to match filenames with [tag1] type tags
# Lagoon (U) [b1].smc
tagPattern = re.compile(r'\[([a-z])+')

# create regex object to match filenames with (U) type region tags
# Rockman X (J) (V1.0) [f1].smc
regionPattern = re.compile(r'\([E|U|G|J]')

# create regex object to match filenames with [!] type tags
# Donkey Kong Country (U) (V1.2) [!].smc
definitivePattern = re.compile(r'\[!\]')



# for each game:
for folder in os.listdir('.'):
    if not folder.startswith('0') and os.path.isdir(folder):





        ''' FOR EACH GAME FOLDER '''

        ''' the following will be done to every folder inside <console>/ that doesn't start with '0X - '    '''


        gameTitle = ''



        # these get populated for a specific game folder, then emptied before switching to the next game folder
        pureFiles = []
        tagFiles = []
        regionFiles = []
        uFiles = []
        eFiles = []
        jFiles = []
        gFiles = []
        fFiles = []
        definitiveFiles = []
        betaFiles = []
        folders = [
            pureFiles,
            regionFiles,
            tagFiles,
            betaFiles,
        ]

        # just a counter for each file inside a game folder
        numberOfFiles = 0





        print('\n\nOkay here\'s all the shit for ' + folder + ':')


        ''' do the following to each game file inside current game folder '''
        for file in os.listdir(folder):





            '''     FOR EACH GAME FILE     '''
            ''' sort current file into its respective folder above '''


            # init flag switches that describe the filename
            pureFlag = False
            tagFlag = False
            regionFlag = False
            definitiveFlag = False
            betaFlag = False
            htmlFlag = False


            # if the file isn't an html file...
            if not file.endswith('.htm') and not file.endswith('.html'):





                ''' flip above switches depending on the filename  '''

                # check for purity (example: Young Merlin.sfc)
                if '(' not in file and '[' not in file:
                    pureFlag = True
                    #pureFiles.append(file)

                else:
                    # check for region code (example: Warlock (E).smc
                    if '(U).' in file or '(USA)' in file or '(E).' in file or '(G).' in file or '(J).' in file or '(F).' in file or 'japan' in file.lower():
                        regionFlag = True
                        #regionFiles.append(file)

                    # check for definitive mark (example: Super Mario World [!].smc)
                    if definitivePattern.search(file):
                        definitiveFlag = True
                        #definitiveFiles.append(file)

                    # check for tag (example: vortex [b2].sfc)
                    if tagPattern.search(file):
                        tagFlag = True
                        #tagFiles.append(file)

                    # check for beta tag
                    if '(beta)' in file.lower():
                        betaFlag = True
                        #betaFiles.append(file)






                ''' sort current file based on switches flipped '''

                # increment file count of games in folder
                numberOfFiles += 1

                if pureFlag:
                    # Sim Ant.smc
                    pureFiles.append(file)

                else:
                    if regionFlag:
                        # check for region / sim_ant (U).smc
                        regionFiles.append(file)
                        if '(U)' in file or '(USA)' in file:
                            uFiles.append(file)
                        elif '(E)' in file:
                            eFiles.append(file)
                        elif '(J)' in file or 'japan' in file.lower():
                            jFiles.append(file)
                        elif '(G)' in file:
                            gFiles.append(file)
                        elif '(F)' in file:
                            fFiles.append(file)

                    if tagFlag:
                        # check for region / sim_ant (U) [t1].smc
                        tagFiles.append(file)

                    elif betaFlag:
                        betaFiles.append(file)

            # file is a .html file
            else:
                os.system('sudo rm {folder}/'.format(folder=folder) + file)





        pureFlag = False
        regionFlag = False
        tagFlag = False
        betaFlag = False


        gameToClean = ''
        if numberOfFiles == 1:
            if len(pureFiles) > 0:
                gameToClean = pureFiles[0]
                pureFlag = True
            elif len(regionFiles) > 0:
                if len(uFiles) > 0:
                    gameToClean = uFiles[0]
                elif len(eFiles) > 0:
                    gameToClean = eFiles[0]
                elif len(jFiles) > 0:
                    gameToClean = jFiles[0]
                elif len(gFiles) > 0:
                    gameToClean = gFiles[0]
                elif len(fFiles) > 0:
                    gameToClean = fFiles[0]
            elif len(tagFiles) > 0:
                gameToClean = tagFiles[0]
            elif len(betaFiles) > 0:
                gameToClean = betaFiles[0]

        else:
            for i in folders:
                if len(i) > 0:

                    # check pureFiles first
                    if i == pureFiles:
                        gameToClean = pureFiles[0]
                        break


                    # then check regionFiles
                    elif i == regionFiles:

                        # first check uFiles
                        if len(uFiles) > 0:
                            for file in uFiles:
                                if file not in tagFiles and file not in betaFiles:
                                    gameToClean = file
                                    break
                            if gameToClean == '':
                                for file in uFiles:
                                    if '[!]' in file:
                                        gameToClean = file
                                        break
                                if gameToClean == '':
                                    gameToClean = uFiles[0]

                        # then check eFiles
                        elif len(eFiles) > 0:
                            for file in eFiles:
                                if file not in tagFiles and file not in betaFiles:
                                    gameToClean = file
                                    break
                            if gameToClean == '':
                                for file in eFiles:
                                    if '[!]' in file:
                                        gameToClean = file
                                        break
                                if gameToClean == '':
                                    gameToClean = eFiles[0]

                        # then check jFiles
                        elif len(jFiles) > 0:
                            for file in jFiles:
                                if file not in tagFiles and file not in betaFiles:
                                    gameToClean = file
                                    break
                            if gameToClean == '':
                                for file in jFiles:
                                    if '[!]' in file:
                                        gameToClean = file
                                        break
                                if gameToClean == '':
                                    gameToClean = jFiles[0]

                        # then check gFiles
                        elif len(gFiles) > 0:
                            for file in gFiles:
                                if file not in tagFiles and file not in betaFiles:
                                    gameToClean = file
                                    break
                            if gameToClean == '':
                                for file in gFiles:
                                    if '[!]' in file:
                                        gameToClean = file
                                        break
                                if gameToClean == '':
                                    gameToClean = gFiles[0]

                        # then check gFiles
                        elif len(fFiles) > 0:
                            for file in fFiles:
                                if file not in tagFiles and file not in betaFiles:
                                    gameToClean = file
                                    break
                            if gameToClean == '':
                                for file in fFiles:
                                    if '[!]' in file:
                                        gameToClean = file
                                        break
                                if gameToClean == '':
                                    gameToClean = fFiles[0]

                        if gameToClean != '':
                            break

                    # now check tagFiles
                    elif i == tagFiles:
                        for file in tagFiles:
                            if '[!]' in file:
                                gameToClean = file
                                break
                        if gameToClean == '':
                            gameToClean = tagFiles[0]


                    elif i == betaFiles:
                        gameToClean = betaFiles[0]
                        break


        if gameToClean == '':
            gameToClean = os.listdir(os.getcwd() + '/' + folder)[0]

        gameTitle = folder + '{extension}'.format(extension=extensionDict[console][0])


        os.system('sudo mkdir ../{console}_cleaned/{folder}'.format(
            console=console,
            folder=folder))

        os.system('sudo mv {folder}/"{gameToClean}" ../{console}_cleaned/{folder}/{gameTitle}'.format(
            folder=folder,
            gameToClean=gameToClean,
            console=console,
            gameTitle=gameTitle))
















# yo
