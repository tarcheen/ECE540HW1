import re

VOLTAGE = 1
FREQUENCY = 2
DIE_LOCATION = 3

# open CPU dump in Read Only mode
pFile = open("silicon_data.txt","r")

voltage = []
freq    = []
dieLoc  = []

while True:
    # read a single line
    line = pFile.readline()
    # end of the file? exit loop
    if not line:
        break

    # if blank line detected or word "id" detected, SKIP
    if (not line.strip() or "id" in line):
        continue

    match = line.split()

    # insert values to appropriate lists
    voltage.append(match[VOLTAGE])
    freq.append(match[FREQUENCY])
    dieLoc.append(match[DIE_LOCATION])

pFile.close()