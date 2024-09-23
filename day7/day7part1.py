#Isha Chaudhuri, 09/17

RawList = []
#initalize variable

f = open("input.txt")
#open input file

for line in f.readlines():
    RawList.append(str(line.replace('\n','')))
    #get rid of each newline in the input file to get a chunk of data

tempList = []
my_temp_dict = {}
real_dict = {}
#initialize more variables

for line in RawList:
    bag, contents = line.split("contain ")
    #split by contain
    bagName = bag.replace("bags","bag").replace(".","").replace("bag ","bag").replace("bags ","bag")
    #clean up data before contain 
    temp = contents.split(", ")
    #split data after contain by comma to get how much of each inner bag there is
    for bags in temp:
        if bags == "no other bags.":
            my_temp_dict ["none"] = 0
            break
            #function stops
        splitBag = bags.split(" ", 1)
        #getting the number before the bag type
        number = splitBag[0]
        label = splitBag[1].replace("bag ","bag").replace("bags ","bag").replace("bags","bag").replace(".","")
        #assign the number to number and the bag type to label and also clean up the bag type data
        my_temp_dict [label] = number
        #add the label, number pair to a temporary dictionary 
    real_dict [bagName] = my_temp_dict
    #add temporary dictionary to real dictionary 
    my_temp_dict = {}
    #clear temp dict

shinyGoldBagCounter = 0
#initialize counter variable
def checkForShinyGoldBag(bag):
    #define recursive function with bag as the paramter
    global shinyGoldBagCounter
    #global variable so its value can be changed inside the function
    if bag == "shiny gold bag":
        shinyGoldBagCounter +=1 
        return True
        #if the bag contains a shiny gold bag, then add 1 to the counter and indicate that the specifications of the function have been met
    if bag in real_dict:
        for inner_bag in real_dict[bag]:
            if inner_bag != "none" and checkForShinyGoldBag(inner_bag):
                return True
            #for each inner bag, if the bag is not empty and the function returns true, return it true again
    return False

for bag in real_dict.keys():
    if bag != "shiny gold bag":  
        checkForShinyGoldBag(bag)
        #this checks each bag that is not a shiny gold bag for the possibility of a shiny gold bag inside of it
        
print(shinyGoldBagCounter)
#print(real_dict)
