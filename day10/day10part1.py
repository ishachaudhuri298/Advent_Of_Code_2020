# list, sort list, ascending order, start from 0, find the 1,2,3 voltage
# break loop once u get a diff of 3 and go to the next index in the list
#keep track of rating ur currently on 
#and counter/accumlator variables

inputList = []
oneVoltage = 0
twoVoltage = 0
threeVoltage = 0
charger = 0
accumulator = 0
#initialize 

#isha 10/17
f = open("input.txt")

for line in f.readlines():
    inputList.append(int(line))

inputList.sort()
#print(inputList)
#sort input file in ascending order

deviceChargingCapacity = inputList[-1]
maxCharging = int(deviceChargingCapacity) + 3
#find the highest charging capacity then the max charging capacity of the adapter

print(deviceChargingCapacity)
charger = 0
#index = 0
inputList.append(maxCharging)

for index in range(0,len(inputList)):
#while inputList[index] != deviceChargingCapacity:
    #this is accessing indexes in the list as opposed to output values
    #charger is supposed to be defined as each corresponding output value based on the index
    if (inputList[index] - charger) == 1:
        #if the charger below the current charger have a difference of 1, add it to the one voltage list
        oneVoltage += 1
    if (inputList[index] - charger) == 2:
        #if the charger below the current charger have a difference of 1, add it to the one voltage list
        twoVoltage += 1
    if (inputList[index] - charger) == 3:
        #if the charger below the current charger have a difference of 3, add it to the three voltage list
        threeVoltage += 1
    charger = inputList[index]

print(oneVoltage)
print(twoVoltage)
print(threeVoltage)
# print(len(inputList))

totalAnswer = oneVoltage * threeVoltage

print(totalAnswer)
