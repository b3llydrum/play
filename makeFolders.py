#! /usr/bin/env python3

import os, sys, time

os.chdir('/Users/davidmaness/Games/roms/atari_2600')

'''
# create one folder for each game
for gameFile in os.listdir('.'):

    # do the following to each file
    if gameFile.endswith('.a26'):

        # find index of first parenthesis
        index = -4
        for char in gameFile:
            if char == '(':
                index = gameFile.index(char)
                break


        # if a folder for the game already exists
        if os.path.isdir(gameFile[:-4]):
            # remove the folder and all its contents
            os.system('sudo rm -rf "{gameFile}"'.format(
                gameFile=gameFile[:-4]))
        if os.path.isdir(gameFile[:index]):
            # remove the folder and all its contents
            os.system('sudo rm -rf "{gameFile}"'.format(
                gameFile=gameFile[:index]))
        # make a folder for the game
        os.system('sudo mkdir "{gameFile}"'.format(
            gameFile=gameFile[:index]))
        print('Created "{gameFolder}"/'.format(
            gameFolder=gameFile[:index]))

    # do the following to each .7z file

    elif gameFile.endswith('.7z'):

        # kill it.
        os.system('sudo rm -rf "{gameFile}"'.format(
            gameFile=gameFile))
        print('Removed "{gameFile}"'.format(
            gameFile=gameFile))

# put best version of game into folder
for file in os.listdir('.'):
    if os.path.isdir(file):

        # if current file is a directory
        # check each file after it until the next directory
        fileList = []
        pureFile = []
        currentFileIndex = os.listdir('.').index(file)
        while not os.path.isdir(os.listdir('.')[currentFileIndex + 1]):
            fileList.append(os.listdir('.')[currentFileIndex + 1])
            currentFileIndex += 1

        if len(fileList) == 1:
            pureFile.append(fileList[0])
        elif len(fileList) > 1:
            for f in fileList:
                if '[!]' in f:
                    pureFile.append(f)
                    break
            if len(pureFile) == 0:
                pureFile.append(fileList[0])

        if len(pureFile) < 1:
            continue

        os.system('sudo mv "{pureFile}" "{folder}"'.format(
            pureFile=pureFile[0],
            folder=file))
        print('Moved "{pureFile}" into "{folder}"'.format(
            pureFile=pureFile[0],
            folder=file))

# remove all extra files
for file in os.listdir('.'):
    if file.endswith('.a26'):
        os.system('sudo rm "{file}"'.format(
            file=file))
'''






for folder in os.listdir('.'):
    if folder[:-1] == ' ':
        os.rename(folder, folder[:-1])
        print('Now called {folder}'.format(folder=folder))

for folder in os.listdir('.'):
    print('\n')
    if '.py' in folder or folder.startswith('.'):
        continue
    if folder[-1] == ' ':
        folder = folder[:-1]
    newFolderName = ''
    for i in range(len(folder)):
        if folder[i] == ' ' and folder[i - 1] != '-':
            newFolderName += '_'
        elif folder[i] == '-' and folder[i - 1] != ' ':
            newFolderName += folder[i]
        else:
            if folder[i].isalpha() or folder[i].isdigit() or folder[i] == '_':
                newFolderName += folder[i].lower()
    if newFolderName.endswith('_the'):
        newFolderName = newFolderName[:-4]

    folder = folder + ' '

    os.system('sudo mkdir {newFolderName}'.format(newFolderName=newFolderName))
    print('Made {newFolderName}/\n'.format(newFolderName=newFolderName))
    time.sleep(2)
    command = 'sudo mv \"{folder}\"/* {newFolderName}'.format(
        folder=folder,
        newFolderName=newFolderName)
    os.system(command)
    print(folder + ' was renamed ' + newFolderName + '\n')
    time.sleep(2)
    os.system('sudo rm -rf \"{folder}\"'.format(
        folder=folder))
    print('Removed \"{folder}\"\n'.format(folder=folder))
    time.sleep(2)
