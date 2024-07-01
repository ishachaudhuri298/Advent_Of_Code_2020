#Isha Chaudhuri, 07/01
numbers = []
numbers2 = []
f = open("input.txt")

for item in f.readlines():
    numbers.append(int(item))
numbers2 = numbers.copy()
# have code sort through both lists and add each number from each list together and see which number pair sums to 2020, print successful pair, after that multiply pair together

for value1 in numbers:
    for value2 in numbers2:
        sum = value1 + value2
        if sum == 2020:
            print (value1 * value2)
            break