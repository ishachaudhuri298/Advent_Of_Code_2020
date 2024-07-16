#Isha Chaudhuri, 07/16

goodPasswords = 0
badPasswords = 0
#creating a variable to store the number of good and bad passwords 

f = open("input.txt")
#opening the input file

for item in f.readlines():
    #for loop that reads through each line of the input file 
    number, letter, password = item.split()
    #splits each line in the input into its specific number, letter, and password
    letter = letter[0]
    #first character in string so here it is removing the letter from the colon
    lower,upper = number.split("-")
    #splits each rule for the numbers into the lower number and the upper number
    totalNumberOfLetters = password.count(letter)
    #counts how many letters are in each password and assigns to a variable
    if (int(lower) <= totalNumberOfLetters) and (int(upper) >= totalNumberOfLetters):
        goodPasswords += 1
        #if the total number of letters meets the rule, then the goodPasswords variable adds one for each correct password
    else:
        badPasswords += 1
        #if the password does not meet the rule, the badPasswords variable adds one

print (goodPasswords)
print (badPasswords)
#both variables are printed 

   