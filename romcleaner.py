#! /usr/bin/env python3


'''''''''''''''''''''''''''''''''''''''''''''
#                DOC HAIKU                  #
#          provides some simple help        #
#        with renaming all your roms        #
#           with consistency                #
#                                           #
'''''''''''''''''''''''''''''''''''''''''''''


import re
import os
import shutil
import sys
from function import *



# try to change directory to rom folder on flash drive
consolesPath = getConsolesPath()


# create list of known consoles from rom folder
consoleList = [system for system in os.listdir(consolesPath)]


# print readable string containing every console for user to choose from
for console in consoleList:
    print(console)
print('\n')


# ask user which console folder they want to clean up
console = getConsoleFromUser(consoleList)






''' once console folder is chosen,
        create backup folder on which to operate
            and create new folder to paste everything into  '''


# create backup folder for uncleaned console folder


print('Copying into backup folder for safety...')                       # Copying into backup folder for safety...

# first delete any existing backup folder
if os.path.exists(console + '_bkp'):
    os.system('sudo rm -rf ' + console + '_bkp')
# then copy console folder into backup folder
os.makedirs(console + '_bkp')
os.system('sudo cp -R ' + console + '/ ' + console + '_bkp')

# create destination folder
if os.path.exists(console + '_cleaned'):
    os.system('sudo rm -rf ' + console + '_cleaned')
os.makedirs(console + '_cleaned')
print('... and created destination folder for clean files.\n')          # ... and created destination folder for clean files.


# switch to backup console folder
os.chdir(console + '_bkp')












''' initialize stuff for the cleaning process '''



buffer_file = ''

regions = ['U', 'J', 'E', 'G']

# create regex object to match filenames with no tags
purePattern = re.compile(r'[^\]][^\)]\.(smc|sfc)')

# create regex object to match filenames with [tag1] type tags
tagPattern = re.compile(r'\[([a-z])+')

# create regex object to match filenames with (U) type region tags
regionPattern = re.compile(r'\([E|U|G|J]')

# create regex object to match filenames with [!] type tags
definitivePattern = re.compile(r'\[!\]')


# string.index(str, beg=0 end=len(string))












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
                os.system('sudo rm ' + folder + '/' + file)


                ''' the following switches the flags initialized above depending on the filename  '''

            else:

                # check for purity (example: young_merlin.sfc)
                if '(' not in file and '[' not in file:
                    pureFlag = True
                    pureFiles.append(file)


                # check for tag (example: vortex [b2].sfc)
                if tagPattern.search(file):
                    tagFlag = True
                    tagFiles.append(file)

                # check for region code (example: warlock (E).smc
                if '(E).smc' in file or '(E).sfc' in file or '(U).smc' in file or '(U).sfc' in file or '(G).smc' in file or '(G).sfc' in file or '(J).smc' in file or '(J).sfc' in file or '(F).smc' in file or '(F).sfc' in file:
                    regionFlag = True
                    regionFiles.append(file)

                # check for definitive mark (example: super_mario_world [!].smc)
                if definitivePattern.search(file):
                    definitiveFlag = True
                    definitiveFiles.append(file)

                # check for beta tag
                if '(beta)' in file.lower():
                    betaFlag = True
                    betaFiles.append(file)







                # increment file count of games in folder
                if not htmlFlag:
                    numberOfFiles += 1


        # when done checking all the files in a games folder:

        # CREATE NEW FOLDER FOR EACH GAME                                               # THIS WHOLE SECTION NEEDS TO BE RE-HARDCODED




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





        # if there are any files in regionFiles, check if there's already a folder in *_new and plop it over
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
                            title += '_'
                        else:
                            title += i.lower()
                    # plop it over
                    if not os.path.isdir('../snes_cleaned/' + folder):
                        os.system('sudo mkdir ../snes_cleaned/' + folder)
                        os.system('sudo chmod 775 ../snes_cleaned/' + folder)
                    print('Region: ' + title)
                    os.system('sudo mv \"' + folder + '\"/\"' + game + '\" ../snes_cleaned/' + folder + '/' + title)
                    #print('Created ../snes_new/' + title[:-4] + '/' + title)
                else:
                    print('Region file, but it\'s dirty.')
        else:
            print('No region files.')






        print('\n')
        gameTitle = ''.join(gameTitle)

'''

        if len(pureFiles) > 0 and len(definitiveFiles) > 0 and len(regionFiles) > 0:
            try:
                os.makedirs('../' + console.lower() + '_new' + '/' + gameTitle)
                print('\nCreated new folder titled ' + gameTitle)
            except FileExistsError:
                print('Folder ' + gameTitle + ' already exists.')
        else:
            pass



        # START COPYING FILES HERE

        # if we have a pure copy, choose it and only it as the English ROM
        if len(pureFiles) > 0:
            try:
                shutil.copyfile(folder + '/' + pureFiles[0], '../' + console.lower() + '_new' + '/' + gameTitle + '/' + gameTitle)
            except FileExistsError:
                print('File ' + gameTitle + ' already exists.')
            except FileNotFoundError:
                print('File ' + gameTitle + ' not found.')
            except IsADirectoryError:
                print(gameTitle + ' is already a directory.')
            except shutil.SameFileError:
                print('Same file.')

        # ...but if we don't have a definitive copy, choose one (U) ROM to be our English ROM
        elif len(definitiveFiles) > 0:
            for game in definitiveFiles:
                if '(U)' in game and game not in tagFiles and game not in betaFiles:
                    game = game[:-4]
                    try:
                        shutil.copyfile(folder + '/' + game, '../' + console.lower() + '_new' + '/' + gameTitle + '/' + game)
                    except FileExistsError:
                        print('File ' + game + ' already exists.')
                    except FileNotFoundError:
                        print('File ' + game + ' not found.')
                    except shutil.SameFileError:
                        print('Same file.')

        # if there is a (J) file, copy it over as well
        if len(regionFiles) > 0:
            for game in regionFiles:
                if '(J)' in game and game not in tagFiles and game not in betaFiles:
                    game = game[:-4]
                    try:
                        shutil.copyfile(folder + '/' + game, '../' + console.lower() + '_new' + '/' + gameTitle + '/' + game)
                        break
                    except FileExistsError:
                        print('File ' + game + ' already exists.')
                    except FileNotFoundError:
                        print('File ' + game + ' not found.')
                    except shutil.SameFileError:
                        print('Same file.')

        # put betas over too
        if len(betaFiles) > 0:
            game = betaFiles[0]
            if game in tagFiles:
                index = game.index('[')
                game = game[:index - 1]
            try:
                shutil.copyfile(folder + '/' + betaFiles[0], '../' + console.lower() + '_new' + '/' + gameTitle + '/' + game)
            except FileExistsError:
                print('File ' + game + ' already exists.')
            except FileNotFoundError:
                print('File ' + game + ' not found.')
            except shutil.SameFileError:
                print('Same file.')
'''
