import os
import glob
import shutil

# Make new folder to hold old files
path = "/Users/tomtom/Downloads/AutomateThis/original"
if not os.path.exists(path):
    os.makedirs(path)


def findStop(lines):
    '''Finds the index of when the #COLOURS list ends'''
    for i in range(7, len(lines)):
        if lines[i] == "\n":
            return i
    return 0


def startRename(typeNumber=0):
    '''Renames files within local directory based on the type of product'''
    if typeNumber == 0:
        shutil.copy(files[0], path)
        os.rename(files[0], "{}-Turkish-{}-{}.jpg".format(style,
                                                          category, types[0]))
    elif typeNumber == 1:
        count = 0
        for i in range(1, findStop(lines)-7+1):
            shutil.copy(files[i], path)
            os.rename(files[i], "{}-{}-Turkish-{}-{}.jpg".format(style,
                                                                 colours[count], category, types[1]))
            count += 1

    elif typeNumber == 2:
        count = 0
        for i in range(findStop(lines)-7+1, len(files)):
            shutil.copy(files[i], path)
            os.rename(files[i], "{}-{}-Turkish-{}-{}.jpg".format(style,
                                                                 colours[count], category, types[2]))
            count += 1

    else:
        print("Error: typeNumber incorrect")


# Store contents read from config text file to separate lists
with open("config.txt") as config:
    lines = config.readlines()
    style = lines[1].strip()
    category = lines[4].strip()
    colours = [s.rstrip().replace(" ", "-") for s in lines[7:findStop(lines)]]
    types = [s.rstrip() for s in lines[findStop(lines)+2:]]
config.close()

# Filter out trailing '\n' for clean lists
files = list(filter(os.path.isfile, glob.glob("*.jpg")))
files.sort(key=lambda x: os.path.getmtime(x))

# Renaming Protocols
# for i in files:
#     print(i)

# print(len(files))
# print(len(colours))

if len(files) == len(colours)*2 + 1:
    for i in range(3):
        startRename(i)
else:
    print("N number of files are not enough to fulfill all colours for each types")

print("Executed!")
