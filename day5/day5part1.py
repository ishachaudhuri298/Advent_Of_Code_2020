#Isha Chaudhuri, 07/24
#looking for highest boarding pass key
#row *8 + column

#used solution for math function and setting the seat ID as the highest one and for lines 35 and 44

import math
#import math to help with rounding numbers

highestSeatID = 0
#create variable for the highest seatID

f = open("input.txt")
#open input file with boarding passes

for f in f.readlines():
    #for each line in the input, do the following
    rows = f[:7]
    #assign the row of the flight to the first 6 characters
    columns = f[7:10]
    #assign the column of the flight to the last 3 characters
    lowestRow = 0
    highestRow = 127
    #create parameters for the rows that reset for each boarding pass
    lowestColumn = 0
    highestColumn = 7
    #create parameters for the columns that reset for each boarding pass
    for item in rows:
        if item == "F":
            highestRow = math.floor(highestRow - ((highestRow - lowestRow)/2))
            #for each letter F, take the lower half of the rows present (floor rounds down)
        if item == "B":
            lowestRow = math.ceil(lowestRow + ((highestRow - lowestRow)/2))
            #for each B, take the upper half of the rows present (ceil rounds up)
    row = lowestRow
    #set the lowestRow to row for the seatID
    for item in columns:
        if item == "L":
            highestColumn = math.floor(highestColumn - ((highestColumn - lowestColumn)/2))
            #for each letter F, take the left half of the rows present (floor rounds down)
        if item == "R":
            lowestColumn = math.ceil(lowestColumn + ((highestColumn - lowestColumn)/2))
            #for each B, take the right half of the rows present (ceil rounds up)
    column = lowestColumn
    #set the lowestColumn to column for the seatID
    seatID = (row * 8) + column
    #calculate the seatID per individual boarding pass
    if (seatID > highestSeatID):
        #if the current seatID is higher than the previous highest seatID, make it the new highest seatID
        highestSeatID = seatID

print(highestSeatID)
#print final highestSeatID