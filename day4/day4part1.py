#Isha Chaudhuri, 07/18

#Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

invalidPassports =0
validPassports = 0
#variables for invalid and valid passports

f = open("input.txt")
#open input file

necessary1 = "byr"
necessary2 = "eyr"
necessary3 = "iyr"
necessary4 = "pid"
necessary5 = "hcl"
necessary6 = "hgt"
necessary7 = "ecl"
#state all necessary keywords
necessary = necessary1 and necessary2 and necessary3 and necessary4 and necessary5 and necessary6 and necessary7
#make all necessary keywords into a string

for item in f.readlines():
    #read through each line of code
    item.split("\n")
    #split code by empty space into lists
    password = str(item)
    #create variable that holds the password
    if necessary in password:
        validPassports += 1
        #if necessary info is in the password, a point is added to valid passwords
    else:
        invalidPassports += 1
        #if necessary info is not there, a point is added to invalid passwords

print(validPassports)
print(invalidPassports)
#print both variables
