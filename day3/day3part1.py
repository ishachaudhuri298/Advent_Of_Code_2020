#Isha Chaudhuri, 07/17
#Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
#must repeat input tree map for as long as it takes to reach the bottom line of trees

#used solution for slope/position

trees = 0
space = 0
#creating variables to count the number of trees and the space where the sled is

f = open("input.txt")
#opening tree map

for line in f.readlines():
#reads through each line in the input file, as opposed to each character
    if line[space] == "#":
        #if the position in the input list has a #, then a point is added to the tree counter
        trees += 1
    space += 3
    #regardless of whether or not the space is a tree or not, the location is moved 3 to the right, and the 1 down comes from the readlines because the code is reading line by line
    if space > 30:
        space = space - 31
        #there are 30 spaces across, so if the space was going too far, it would move down to the next line

print(trees) 
#print the final amount of trees 



