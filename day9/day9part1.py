#Isha Chaudhuri
#10/10
#The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?

#used solution for lines 25-27

f = open("input.txt")
#open input file

allData = []
possibleSums = []
dataBefore25 = []
validNumbers = []
#initalize variables

for line in f.readlines():
    allData.append(int(line))
#append all data to a list
    dataAfter25 = allData[25:]
    #print(dataAfter25)
    for number in dataAfter25:
            #for each line greater than the 25th line, add all the data before it to a list
            dataBefore25 = dataAfter25[number-25:number]
            #for each value in data after 25, create a new list with the 25 numbers directly before it
            for number1 in dataAfter25:
                for number2 in dataAfter25:
                    if (number1 != number2):
                        sum = number1 + number2
                        possibleSums.append(sum)
                        #print(possibleSums)
                        #for each 25 numbers before a specific number, if those two add to the number, add it to a list
            if number in (possibleSums):
                validNumbers.append(number)
                #if the specific number has two numbers that add up to it in the previous 25 numbers, add it to a list
            dataBefore25 = []
            possibleSums = []

print(validNumbers)