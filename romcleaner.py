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
from patterns import *



# ~/Games/roms/
consolesPath = getConsolesPath()


# every console folder in consolesPath
consoleList = [system for system in os.listdir(consolesPath)]


# print every console for user to choose from
for console in consoleList:
    print(console)
print('\n')



# ask user which console folder they want to clean up
# snes
console = getConsoleFromUser(consoleList)
extension = extensionDict[console][0]


# change directory to the parent of console
os.chdir(consolesPath)



''' once console folder is chosen,
        create backup folder on which to operate
            and create new folder to paste everything into  '''


# create backup folder for uncleaned console folder

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


# and at the end, replace the original console folder with the _cleaned folder



























''' this next part looks through the game folders and organizes the game files '''




# switch to backup console folder
os.chdir(console + '_working')
print('Moved to {console}_working/ folder to do operations.'.format(console=console))
time.sleep(2)



# data imported from patterns.py




# for each game:
for folder in os.listdir('.'):
    if not folder.startswith('0') and os.path.isdir(folder):



        ''' the following will be done to every folder inside <console>/ that doesn't start with '0X - '    '''


        gameTitle = ''



        # these get populated for a specific game folder, then emptied before switching to the next game folder
        pureFiles = []
        tagFiles = []
        regionFiles = []
        definitiveFiles = []
        betaFiles = []

        # just a counter for each file inside a game folder
        numberOfFiles = 0





        print('\nOkay here\'s all the shit for ' + folder + ':')




        # for each file in the current game folder:
        for file in os.listdir(folder):



            ''' the following is done for each file inside the game folder  '''





            # init flags that describe the filename
            pureFlag = False
            tagFlag = False
            regionFlag = False
            definitiveFlag = False
            betaFlag = False
            htmlFlag = False




            # filter html files and DESTORY THEM
            if file.endswith('htm') or file.endswith('.html'):
                os.system('sudo rm {folder}/'.format(folder=folder) + file)


                ''' the following switches the flags initialized above depending on the filename  '''

            else:

                # check for purity (example: young_merlin.sfc)
                if '(' not in file and '[' not in file:
                    pureFlag = True
                    #pureFiles.append(file)

                else:
                    # check for region code (example: warlock (E).smc
                    if '(E).smc' in file or '(E).sfc' in file or '(U).smc' in file or '(U).sfc' in file or '(G).smc' in file or '(G).sfc' in file or '(J).smc' in file or '(J).sfc' in file or '(F).smc' in file or '(F).sfc' in file:
                        regionFlag = True
                        #regionFiles.append(file)

                    # check for definitive mark (example: super_mario_world [!].smc)
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


                if pureFlag:
                    pureFiles.append(file)  # sim_ant.smc
                else:
                    if regionFlag and not betaFlag and not tagFlag:
                        regionFiles.append(file)  # check for region / sim_ant (U).smc
                    elif regionFlag and not betaFlag:
                        tagFiles.append(file)  # check for region / sim_ant (U) [t1].smc
                    elif not regionFlag and not betaFlag:
                        tagFiles.append(file)  # probably a different version / sim_ant [b4].smc
                    elif betaFlag:
                        betaFiles.append(file)





                # increment file count of games in folder
                if not htmlFlag:
                    numberOfFiles += 1


        # when done checking all the files in a games folder:

        # CREATE NEW FOLDER FOR EACH GAME

        # THIS WHOLE SECTION IS HARD-CODED FOR SNES


        # PRIORITIZE PURE FILES. IF THERE'S A PURIFIED FILE, COPY IT OVER

        #print('Here\'s all the pure stuff:')
        # if there is anything in pureFiles, create a folder for the game in *_new and plop it in there

        if len(pureFiles) > 0:
            '''
            print('Here are all the pure files for ' + folder)
            for i in pureFiles:
                print(i)
            print('\n')
            '''
            title = ''                              # title becomes definitive version  --  aladdin.sfc
            gameTitle = pureFiles[0]
            gameTitle = list(gameTitle)
            for i in gameTitle:
                if i == ' ':
                    title += '_'
                elif i == '\'':
                    pass
                elif i == '!':
                    pass
                else:
                    title += i.lower()
            if os.path.isdir('../snes_cleaned/' + folder):
                os.system('sudo rm -rf ../snes_cleaned/' + folder)
            os.system('sudo mkdir ../snes_cleaned/' + folder)
            os.system('sudo chmod 775 ../snes_cleaned/' + folder)
            extension = title[-4:]
            print('Pure: ' + title)
            os.system('sudo mv \"' + folder + '\"/\"' + pureFiles[0] + '\" ../snes_cleaned/' + folder + '/' + folder + extension)
            #print('Created ../snes_new/' + title[:-4] + '/' + title + '')
        else:
            print('No pure file.')




        # if there are any files in regionFiles, check if there's already a folder in *_cleaned and plop it over
        # ONLY IF it's not also in betaFiles and tagFiles


        #print('Here\'s all the region stuff:')

        if len(regionFiles) > 0:
            # do the following for each foreign version of the game
            for game in regionFiles:
                '''
                print('Here are all the region files for ' + folder)
                for i in regionFiles:
                    if i not in betaFiles or i not in tagFiles:
                        print(i)
                print('\n')
                '''



                # create an empty version of the renamed file
                if ').sfc' in game or ').smc' in game:
                    # clean title
                    title = ''
                    for i in list(game):
                        if i == ' ':
                            title += '_'
                        elif i == '\'' or i == '!':
                            pass
                        elif i == '(' or i == ')':
                            pass  # this causes __j_. Change to pass to make it _j
                        else:
                            title += i.lower()
                    # plop it over
                    if not os.path.isdir('../snes_cleaned/' + folder):
                        os.system('sudo mkdir ../snes_cleaned/' + folder)
                        os.system('sudo chmod 775 ../snes_cleaned/' + folder)
                    print('Region: ' + title)
                    os.system('sudo mv \"' + folder + '\"/\"' + game + '\" ../snes_cleaned/' + folder + '/' + title)
                    #print('Created ../snes_cleaned/' + title[:-4] + '/' + title)
                else:
                    print('Region file, but it\'s dirty.')



        elif len(tagFiles) > 0:

            for game in tagFiles:

                # clean title
                title = ''
                for i in list(game):

                    if i == ' ':
                        title += '_'
                    elif i == '\'' or i == '!' or i == '\"':
                        pass
                    elif i == '(' or i == ')':
                        pass  # this causes __j_. Change to pass to make it _j
                    else:
                        title += i.lower()
                # plop it over
                if not os.path.isdir('../snes_cleaned/' + folder):
                    os.system('sudo mkdir ../snes_cleaned/' + folder)
                    os.system('sudo chmod 775 ../snes_cleaned/' + folder)
                print('Tagged: ' + title)
                os.system('sudo mv \"' + folder + '\"/\"' + game + '\" ../snes_cleaned/' + folder + '/' + title)
                #print('Created ../snes_cleaned/' + title[:-4] + '/' + title)









        print('\n')
        gameTitle = ''.join(gameTitle)
