import os
import shutil

# Full directory to your downloads folder. Ex /Users/zach/Downloads/
DOWNLOADSDIR = ''

# Dictionary for defining the folder name and the extensions to be placed in that directory.
filesys = {
    'Books': ['epub'],
    'Compressed': ['zip', 'zipx', 'bz2', '7z', 'rar'],
    'Executables': ['exe', 'dmg', 'app', 'BAT', 'sh'],
    'Images': ['png'],
    'Media': ['mp3', 'mp4'],
    'Other': [],
    'Document': ['pdf']
}

# Will attempt to create all folders listed in the filesys dictionary. Prints to console if already created.
def makeDirs():
    for directory in filesys:
        try:
            os.mkdir(DOWNLOADSDIR + directory)
        except FileExistsError:
            print("already made")

# Loops through every file in the downloads folder and will move to correct directory if extension is found.
def moveFile(file):
    for key in filesys:
        for extension in filesys[key]:
            if file.split('.')[-1] == extension:
                shutil.move(DOWNLOADSDIR+file, DOWNLOADSDIR+key)


os.chdir(DOWNLOADSDIR)
makeDirs()
files = os.listdir()
for file in files:
    moveFile(file)
