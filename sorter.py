import os
import shutil
import random

# Full directory to your downloads folder. Ex /Users/zach/Downloads/
DOWNLOADSDIR = '/Users/zachburns/Downloads/'

# Dictionary for defining the folder name and the extensions to be placed in that directory.
filesys = {
    'Books': ['epub'],
    'Compressed': ['zip', 'zipx', 'bz2', '7z', 'rar'],
    'Executables': ['exe', 'dmg', 'app', 'BAT', 'sh'],
    'Images': ['png', 'JPG'],
    'Media': ['mp3', 'mp4'],
    'Other': ['torrent'],
    'Document': ['pdf', 'doc', 'docx']
}

# Will attempt to create all folders listed in the filesys dictionary. Prints to console if already created.
def makeDirs():
    for directory in filesys:
        try:
            os.mkdir(DOWNLOADSDIR + directory)
        except FileExistsError:
            pass

# Loops through every file in the downloads folder and will move to correct directory if extension is found.
def moveFile(file):
    for key in filesys:
        for extension in filesys[key]:
            if file.split('.')[-1] == extension:
                try:
                    shutil.move(DOWNLOADSDIR+file, DOWNLOADSDIR+key)
                except shutil.Error:
                    renamedFile = file.split('.')[-2] + str(random.randint(100, 999)) + '.' + file.split('.')[-1]
                    os.rename(file, renamedFile)
                    shutil.move(DOWNLOADSDIR+renamedFile, DOWNLOADSDIR+key)


os.chdir(DOWNLOADSDIR)
makeDirs()
files = os.listdir()
for file in files:
    moveFile(file)
