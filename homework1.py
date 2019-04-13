import re


# open CPU dump in Read Only mode
pFile = open("silicon_data.txt","r")

while True:
    # read a single line
    line = pFile.readline()
    # end of the file? exit loop
    if not line:
        break
    print(line)

pFile.close()


'''
sent = "1  0.9	1900                       1,1"

#matchObj = re.split("", sent)

saved = sent.split()
#print(saved[3])

for x in saved:
    print(x)
'''