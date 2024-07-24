#Isha Chaudhuri, 07/22
# day 4 part 2
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

#used solution for lines 94 - 105 and 83 and 88

validPassports = 0
passport = ""
groupList = []
extraValidPassports = 0
validEntries = 0
#variables

f = open("input.txt")
#open input file

necessary = ['byr', 'eyr', 'iyr', 'pid', 'hcl', 'hgt', 'ecl']
#add all necessary keywords to a list
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
 #variable for the valid passports with new contraints

for line in f.readlines():
#apply the code below to each line in the input
    if line != "\n":
        passport = passport + line
        #if the line of code is not a blank line, add it to an empty variable called passport, which stores one passport at a time 
    else:
        groupList.append(passport)
        passport = ""
        #if the line of code is a blank line, add it to the groupList and reset the password variable

validPassportsThatNeedToBeChecked = []
for passport in groupList:
    #for each password, do as follows
    fields = []
    validEntries = 0
    #create a new variable that stores each field of the password separately 
    classifiers = passport.split()
    #split the passport by white space
    for item in classifiers:
        #split each classifier into the necessary keyword and its corresponding data, and add the keyword to the fields variable
        keyword, data = item.split(":")
        fields.append(keyword)
    if all(item in fields for item in necessary):
        #if all necessary keywords are present in the password, add one point to validPassports and add it to a new list to be further checked
        validPassportsThatNeedToBeChecked.append(passport)
        validPassports +=1
    
    for item in validPassportsThatNeedToBeChecked:
        #for each passport that has all the required fields, do the following
        for item in classifiers:
            if keyword == "byr":
                #if the birth year meets the requirements, add it to the validEntries
                if len(data) == 4:
                    if int(data) >= 1920 and int(data) <= 2002:
                        validEntries += 1
            if keyword == "iyr":
                #if the issue year meets the requirements, add it to the validEntries
                if len(data) == 4:
                    if int(data) >= 2010 and int(data) <= 2020:
                        validEntries += 1
            if keyword == "eyr":
                #if the expiration year meets the requirements, add it to the validEntries
                if len(data) == 4:
                    if int(data) >= 2020 and int(data) <= 2030:
                        validEntries += 1
            if keyword == "hgt":
                #if the height meets the requirements, add it to the validEntries
                if data.find("cm") != -1:
                    height = data[:-2]
                    #remove the cm from the data
                    if int(height) >= 150 and int(height) <= 193:
                        validEntries +=1
                if data.find("in") != -1:
                    height = data[:-2]
                    #remove the in from the data
                    if int(height) >= 59 and int(height) <= 76:
                        validEntries += 1
            if keyword == "hcl":
                validCharacters = 0
                #if the hair color meets the requirements, add it to the validEntries
                if data[0] == "#" and len(data) == 7:
                        for j in data:
                            if j.isdigit():
                            #if j is a number, check that it is between 0 and 9 
                                j = int(j)
                                if j >= 0 and j <= 9:
                                    validCharacters += 1
                            elif j.isalpha():
                            #if j is a letter, check that it is between a and f
                                if j >= 'a' and j <= 'f':
                                    validCharacters +=1
                        if validCharacters == 6:
                            validEntries +=1
            if keyword == "pid":
                #if the passport ID meets the requirements, add it to the validEntries
                if len(data) == 9:
                    validEntries += 1
            if keyword == "ecl":
                #if the eye color meets the requirements, add it to the validEntries
                if data in ecl:
                    validEntries += 1
        if validEntries == 7:
            extraValidPassports += 1

print(extraValidPassports)
#print final number of passports