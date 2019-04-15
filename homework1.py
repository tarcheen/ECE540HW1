import matplotlib.pyplot as plt
from operator import itemgetter

VOLTAGE = 0
INDEX = 0
X_VALUE = 0
Y_VALUE = 1
FREQUENCY = 1
X_LOCATION = 2
Y_LOCATION = 3

# open CPU dump in Read Only mode
pFile = open("silicon_data.txt", "r")

parsedList = []

while True:
    # read a single line
    line = pFile.readline()
    # end of the file? exit loop
    if not line:
        break

    # if blank line detected or word "id" detected, SKIP
    if (not line.strip() or "id" in line):
        continue

    # split all values by whitespace
    match = line.split()

    # split die locations by comma
    locations = match[3].split(",")
    # die locations saved, pop the last element which includes the location
    match.pop()
    # pop the first element as well, numbers not needed
    match.pop(INDEX)
    # insert xLocation to list
    match.append(locations[X_VALUE])
    # insert yLocation to list
    match.append(locations[Y_VALUE])

    parsedList.append(match)

pFile.close()

# sort list elements in respect to y-values
sortedParsedList = sorted(parsedList, key=itemgetter(Y_LOCATION))

# all contents are read, now lets write everything to new file
pFile = open("sorted_data.txt", 'w')

# write the titles
pFile.write("#id\tvoltage(V)\tfrequency(Mhz)\tDieLocation(x,y)\n\n")

# write all sorted values to file, plot all the values
for counter, x in enumerate(sortedParsedList):
    pFile.write(str(counter + 1) + "\t\t" + str(x[VOLTAGE]) + "\t\t" + str(x[FREQUENCY]) + "\t\t" + str(
        x[X_LOCATION]) + "," + str(x[Y_LOCATION]) + "\n")
    plt.scatter(x[VOLTAGE], x[FREQUENCY])

# done, close the file
pFile.close()

# display the plots
plt.show()
