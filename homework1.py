'''
Hamed Mirlohi
ECE 510 Post-Silicon Validation
Homework #1

github: https://github.com/tarcheen/ECE540HW1
'''

import matplotlib.pyplot as plt
from operator import itemgetter

VOLTAGE = 0
INDEX = 0
X_VALUE = 0
Y_VALUE = 1
FREQUENCY = 1
X_LOCATION = 2
Y_LOCATION = 3
DIE_X_Y = 3


def process_Line(line):
    # split all values by whitespace
    match = line.split()

    # split die locations by comma
    locations = match[DIE_X_Y].split(",")
    # die locations saved, pop the last element which includes the location
    match.pop()
    # pop the first element as well, enumerated numbers not needed
    match.pop(INDEX)
    # insert xLocation to list
    match.append(locations[X_VALUE])
    # insert yLocation to list
    match.append(locations[Y_VALUE])

    return match


# open CPU dump in Read Only mode
with open("silicon_data.txt", "r") as pFile:
    parsedList = []

    while True:
        # read a single line
        line = pFile.readline()
        # end of the file? if yes, exit the while loop
        if not line:
            break

        # if blank line detected or word "id" detected, SKIP
        if (not line.strip() or "id" in line):
            continue
        # storing every lines element as a list
        parsedList.append(process_Line(line))

# sort list elements in respect to x-values first, then y-values
sortedParsedList = sorted(parsedList, key=itemgetter(X_LOCATION, Y_LOCATION))

# all contents are read, now lets write everything to new file
with open("sorted_data.txt", 'w') as sFile:
    # write the titles
    sFile.write("#id\tvoltage(V)\tfrequency(Mhz)\tDieLocation(x,y)\n\n")

    # write all sorted values to file, plot all the values
    for counter, x in enumerate(sortedParsedList):
        sFile.write(str(counter + 1) + "\t\t" + str(x[VOLTAGE]) + "\t\t" + str(x[FREQUENCY]) + "\t\t" + str(
            x[X_LOCATION]) + "," + str(x[Y_LOCATION]) + "\n")
        # plot voltage and frequency
        plt.scatter(x[VOLTAGE], x[FREQUENCY])

# display the plots
plt.show()
