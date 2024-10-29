#isha, 10/22

#rules for seat change: If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.
# adjacent = the seat above, below, left, to the right, and the 4 diagonals 
#run through code until seats are unchanged and calculate how many seats are occupied

#figure out a way to create a new list inside the big list of the adjacent seats then everything will be easier and i can just follow the rules
#maybe like [space + 1 space -1 idk]

#can use list function to split each line up by character and then store a variable for the line before it and line after it and current line
inputFile = []
currentRow = []
beforeRow = []
afterRow = []
occupiedSeats = 0

f = open("input.txt")
# testFile = []
# testFile.append("LLLLL.LLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.L.LLLLLL.LLLLLL.LLL.LLLLLLLL.LLLLL.L.LLLLLLLLLLLLLLLL.LLLLLLL"
# )
# print(len(testFile))

for line in f.readlines():
    inputFile.append(line)
    for item in range(0,len(inputFile)+1):
        #for every line in the inputfile
        row = list(inputFile[item])
        currentRow.append(row)
        beforeRow.append(list(inputFile[item-1]))
        #append each row before current row to a list
        afterRow.append(list(inputFile[item+1]))
        #append each row after current row to a list
        # for item in currentRow:
        #     #need to define item as an index
        #     if item == "L" and currentRow[item+1] == "L" and currentRow[item-1] == "L" and 
        for index in range(0,len(row)):
            if currentRow[index] == "#":
                #this is to check if the seat is occupied and 4 or more seats adjacent is occupied, the seat becomes empty
                occupiedSeats += 1
                occupiedSeatCounterTemp = 0
                if currentRow[index+1] == "L":
                    occupiedSeatCounterTemp += 1
                if currentRow[index-1] == "L":
                    occupiedSeatCounterTemp += 1
                if beforeRow[index-1] == "L":
                    occupiedSeatCounterTemp += 1
                if beforeRow[index] == "L":
                    occupiedSeatCounterTemp += 1
                if beforeRow[index+1] == "L":
                    occupiedSeatCounterTemp += 1
                if afterRow[index-1] == "L":
                    occupiedSeatCounterTemp += 1
                if afterRow[index] == "L":
                    occupiedSeatCounterTemp += 1
                if afterRow[index+1] == "L":
                    occupiedSeatCounterTemp += 1
                if occupiedSeatCounterTemp > 3:
                    occupiedSeats -= 1
            if currentRow[index] == "L":
                #this is to check and see if the seat is empty and there are no occupied seats adjacent to it, then it switches it to an occupied seat
                emptySeatCounter = 0
                if (currentRow[index+1] == "L"):
                    emptySeatCounter += 1
                if (currentRow[index-1] == "L"):
                    emptySeatCounter += 1
                if (beforeRow[index] == "L"):
                    emptySeatCounter += 1
                if (beforeRow[index-1] == "L"):
                    emptySeatCounter += 1
                if (beforeRow[index+1] == "L"):
                    emptySeatCounter += 1
                if (afterRow[index] == "L"):
                    emptySeatCounter += 1
                if (afterRow[index+1] == "L"):
                    emptySeatCounter += 1
                if (afterRow[index-1] == "L"):
                    emptySeatCounter += 1
                if emptySeatCounter == 8:
                    occupiedSeats += 1

print(occupiedSeats)