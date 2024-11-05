#day11part1 redo
#isha chaudhuri

inputFile = []
currentRow = []
beforeRow = []
afterRow = []
occupiedSeats = 0
totalOccupiedSeats = -1

f = open("input.txt")

for line in f.readlines():
    inputFile.append(line)

#create function and check for the conditions
def adjacentSeatCounter (indexHor, indexVert, currentRow, beforeRow, afterRow):
    try:
        occupiedSeatCounterTemp = 0
        if indexHor < 97:
        # all non right end seats
            if currentRow[indexHor+1] == "L":
                occupiedSeatCounterTemp += 1
        if indexHor > 0:
        # all non left end seats
            if currentRow[indexHor-1] == "L":
                occupiedSeatCounterTemp += 1
        if indexHor > 0 and indexVert > 0:
        # eliminating top left corner
            if beforeRow[indexHor-1] == "L":
                occupiedSeatCounterTemp += 1
        if indexHor < 97 and indexVert > 0:
        # eliminating top right corner
            if beforeRow[indexHor+1] == "L":
                occupiedSeatCounterTemp += 1
        if indexHor > 0 and indexVert < 90:
        # eliminating bottom left corner
            if afterRow[indexHor-1] == "L":
                occupiedSeatCounterTemp += 1
        if indexHor < 97 and indexVert < 90:
        # eliminating bottom right corner
            if afterRow[indexHor+1] == "L":
                occupiedSeatCounterTemp += 1
        if indexVert > 0:
        # eliminating top row
            if beforeRow[indexHor] == "L":
                occupiedSeatCounterTemp += 1
        if indexVert < 90:
        # eliminating bottom row 
            if afterRow[indexHor] == "L":
                occupiedSeatCounterTemp += 1
    except Exception as e:
        print(indexHor,indexVert)
    return occupiedSeatCounterTemp 

while totalOccupiedSeats is not occupiedSeats:
    for indexVert, y in enumerate(inputFile):
        #for every line in the inputfile
        row = list(inputFile[indexVert])
        currentRow = row
        if indexVert > 0:
            beforeRow = (list(inputFile[indexVert-1]))
        else:
            beforeRow = row
            #so that before row has a value, we won't use it
        #append each row before current row to a list
        if indexVert < 97:
            afterRow = (list(inputFile[indexVert+1]))
        else:
            beforeRow = row
            #combatting the index error
        for indexHor,x in enumerate(row):
            totalSeats = adjacentSeatCounter(indexHor, indexVert, currentRow, beforeRow, afterRow)
            if x == "#":
                occupiedSeats += 1
                if totalSeats > 3:
                #each argument that is passed in line 80 will correspond to same argument passed in the definition of the function
                    occupiedSeats -= 1
            if x == "L":
                if totalSeats == 0:
                    occupiedSeats += 1
    if totalOccupiedSeats is not occupiedSeats:
        totalOccupiedSeats = occupiedSeats 
    else:
        print(occupiedSeats)

                   
                
