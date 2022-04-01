import os, shutil

for folderName, subFolders, fileNames in os.walk('D:\\pythonSTUFF\\'):
    print('The current folder is '+ folderName)

    for subfolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
        if filename[-3:] == 'jpg':
            shutil.copy('D:\\pythonSTUFF\\'+filename, 'D:\\pythonSTUFF\\SelectCopyFolder\\')

    print('')

