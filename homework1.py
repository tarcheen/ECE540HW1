import re
import matplotlib.pyplot as plt
from operator import itemgetter

#VOLTAGE = 1
#FREQUENCY = 2
#DIE_LOCATION = 3

# open CPU dump in Read Only mode
pFile = open("silicon_data.txt","r")

#voltage = []
#freq    = []
#dieLoc  = []

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
    match.pop(0)
    # insert xLocation to list
    match.append(locations[0])
    # insert yLocation to list
    match.append(locations[1])
    # convert all elements to integer
    #match = [ float(x) for x in match]

    parsedList.append(match)
    # insert values to appropriate lists
    #voltage.append(match[VOLTAGE])
    #freq.append(match[FREQUENCY])
    #dieLoc.append(match[DIE_LOCATION])


pFile.close()

#sort list elements in respect to y-values
sortedParsedList = sorted(parsedList, key=itemgetter(3))

# all contents are read, now lets write everything to new file
pFile = open("sorted_data.txt",'w')

#write the titles
pFile.write("#id\tvoltage(V)\tfrequency(Mhz)\tDieLocation(x,y)\n\n")

#write all sorted values to file, plot all the values
for counter, x in enumerate(sortedParsedList):
    pFile.write(str(counter) + "\t\t" + str(x[0]) + "\t\t" + str(x[1]) + "\t\t" + str(x[2])+","+ str(x[3]) + "\n")
    plt.scatter(x[0],x[1])

# done, close the file
pFile.close()

#display the plots
plt.show()
