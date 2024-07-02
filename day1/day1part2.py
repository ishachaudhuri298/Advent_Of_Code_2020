#Isha Chaudhuri, 07/02
#goal: find the product of 3 numbers that sum to 2020
numbers = []
numbers2 = []
numbers3 = []
#created 3 variables to store the input data as 3 lists 

f = open("input.txt")
#opening the given input data

for item in f.readlines():
    numbers.append(int(item))
numbers2 = numbers.copy()
numbers3 = numbers.copy()
#the program will take the input data and create 3 lists with that data

for value1 in numbers:
    for value2 in numbers2:
        for value3 in numbers3:
          sum  = value1 + value2 + value3
          if sum == 2020:
              print (value1 * value2 * value3)
              break

