#Isha Chaudhuri, 07/26
#09/16/24

yes = set()
sum = 0
#sets remove duplicate values
#used solution to learn about sets

f = open("input.txt")
#open input file

for line in f.readlines():
#apply the code below to each line in the input
    for letter in line:
        #for each character in the line, if it is not an empty space, add it to an empty set
        if letter != "\n":
            yes.add(letter)
    if line == "\n":
        #for each character in the line, if it is an empty space, reset the sum variable by adding the letters from each line. this makes it so that each group of letters is added to the set together.
        sum = sum + len(yes)
        yes = set()
        #reset the set variable
if (len(yes) != 0):
    #if the length of the yes variable is not zero, add it to the final sum variable
    sum = sum + len(yes)

print (sum)