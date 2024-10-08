#Isha Chaudhuri, 09/26

f = open("input.txt")
#open input file 

masterList = []
acc = 0
value = 0
linesDone = []
#initialize variables

for line in f.readlines():
    command, number = line.split()
    masterList.append([command, int(number)])
    #split each line in the input file by command and number and add those values to a master list

while value < len(masterList):
    
    lineInCode = masterList[value]
    #assign each item in the master list to the variable "lineInCode"
    
    if value in linesDone:
        break
        #if the same line of code is visited twice, the function stops
    linesDone.append(value)

    command, number = lineInCode

    if command == "acc":
        acc += number
        value += 1
        #to accumulate the values
    elif command == "jmp":
        value += number
        #to jump lines in the code
    else:
        value += 1

print(acc)



