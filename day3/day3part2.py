#isha chaudhuri, 07/17

trees3 = 0
trees1 = 0
trees5 = 0
trees7 = 0
trees12 = 0
space3 = 0
space1 = 0
space5 = 0
space7 = 0
space12= 0
counter = 0

#creating variables to count the number of trees and the space where the sled is
#originally did not have counter variable and was not getting the right answer, but solution had counter variable and I tried it and that worked. what is the counter variable for?

f = open("input.txt")
#opening tree map

for line in f.readlines():
    #if there is a tree in every spot that is 3 right and 1 down, tree will be added to total
    if line[space3] == "#":
        trees3 += 1
    space3 += 3
    if (space3 > 30):
    #once position reaches end of line, it will go back to the beginning because there are 30 spaces
        space3 = space3 - 31

    if line[space1] == "#":
    #code for a tree in every spot that is 1 right and 1 down
        trees1 += 1
    space1 += 1
    if (space1 > 30):
        space1 = space1 - 31

    if line[space5] == "#":
    #code to find trees that are 5 right, 1 down
        trees5 += 1
    space5 += 5
    if (space5 > 30):
        space5 = space5 - 31

    if line[space7] == "#":
    #code to find trees that are 7 right, 1 down
        trees7 += 1
    space7 += 7
    if (space7 > 30):
        space7 = space7 - 31

    if (counter %2 ==0):
        #code for every tree that is 1 right, 2 down
        if line[space12] == "#":
            trees12 += 1
        space12 += 1
        if (space12 > 30):
            space12 = space12 - 31
    counter += 1
    #confused about purpose of counter variable, used solution


totalTrees = trees1 * trees3 * trees5 * trees7 * trees12
#variable to find all the trees

print(totalTrees) 