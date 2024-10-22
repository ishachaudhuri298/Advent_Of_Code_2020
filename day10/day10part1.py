# list, sort list, ascending order, start from 0, find the 1,2,3 voltage
# break loop once u get a diff of 3 and go to the next index in the list
#keep track of rating ur currently on 
#and counter/accumlator variables

inputList = []
oneVoltage = []
threeVoltage = []
charger = 0
accumulator = 0
#initialize 

#isha 10/17
f = open("input.txt")

for line in f.readlines():
    inputList.append(line)

inputList.sort()
#sort input file in ascending order

deviceChargingCapacity = inputList[len(inputList)-1]
maxCharging = int(deviceChargingCapacity) + 3
#find the highest charging capacity then the max charging capacity of the adapter

print(deviceChargingCapacity)

for item in range(0,len(inputList)-1):
    #this is accessing indexes in the list as opposed to output values
    int(item)
    charger = inputList[item]
    #charger is supposed to be defined as each corresponding output value based on the index
    if int(inputList[item+1]) == (int(charger) + 1):
        #if the charger below the current charger have a difference of 1, add it to the one voltage list
        oneVoltage.append(item)
    if int(inputList[item+1]) == (int(charger) + 3):
        #if the charger below the current charger have a difference of 3, add it to the three voltage list
        threeVoltage.append(item)

print(oneVoltage)
print(threeVoltage)

totalAnswer = len(oneVoltage) * len(threeVoltage)

print(totalAnswer)
