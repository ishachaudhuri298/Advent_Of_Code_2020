#Isha Chaudhuri, 07/26
# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

# What is the ID of your seat?

import math
#import math to help with rounding numbers

highestSeatID = 0
allSeatIDS = []
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
    allSeatIDS.append(seatID)
    #calculate the seatID per individual boarding pass and add it to the list of all seat IDS

seatIDS = set(range(0,823))
#create a set with all the possible SeatIDS
allSeatIDS = set(allSeatIDS)
#create a set with all the seatIDS that exist

highestSeatIDRow1 = 12
#the highest seatID a missing seat in the front can have

missingFromFlight = seatIDS - allSeatIDS
#see what values in allSeatIDS are missing from the present seatIDS

missingFromFlight = list(missingFromFlight)
#make the set into a list

for item in missingFromFlight:
    if item > highestSeatIDRow1:
        #if the item is greater than the highestID that is missing, print it out
        print(item)
