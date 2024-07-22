#Isha Chaudhuri, 07/18

#Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

#used solution for lines 18-26

validPassports = 0
passport = ""
groupList = []
#variables

f = open("input.txt")
#open input file

necessary = ['byr', 'eyr', 'iyr', 'pid', 'hcl', 'hgt', 'ecl']
#add all necessary keywords to a list

for line in f.readlines():
#apply the code below to each line in the input
    if line != "\n":
        passport = passport + line
        #if the line of code is not a blank line, add it to an empty variable called passport, which stores one passport at a time 
    else:
        groupList.append(passport)
        passport = ""
        #if the line of code is a blank line, add it to the groupList and reset the password variable


for passport in groupList:
    #for each password, do as follows
    fields = []
    #create a new variable that stores each field of the password separately 
    classifiers = passport.split()
    #split the passport by white space
    for item in classifiers:
        #split each classifier into the necessary keyword and its corresponding data, and add the keyword to the fields variable
        keyword, data = item.split(":")
        fields.append(keyword)
    if all(item in fields for item in necessary):
        #if all necessary keywords are present in the password, add one point to validPassports
        validPassports += 1

print(validPassports)
#print final number
