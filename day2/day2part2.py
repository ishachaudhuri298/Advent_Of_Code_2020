#Isha Chaudhuri, 07/16

goodPasswords = 0
badPasswords = 0
#variables to store the amount of good and bad passwords

f = open("input.txt")
#opening the input file

for item in f.readlines():
    #for loop that reads through each line of the input file 
    number, letter, password = item.split()
    #splits each line in the input into its specific number, letter, and password
    letter = letter[0]
    #first character in string so here it is removing the letter from the colon
    first,second = number.split("-")
    #splits each rule for the numbers into the first and second place it needs to appear in the password
    if (letter == password[int(first)-1]):
        goodPasswords += 1
        #if the letter is in the first place it needs to be, add one to the goodPasswords
        if (letter == password[int(second)-1]):
            goodPasswords -= 1
            badPasswords += 1
            #if the letter is also in the second place it needs to be, subtract one from the goodPasswords and add one to the badPasswords
    if (letter == password[int(second)-1]):
        goodPasswords += 1
        #if the letter is in the second place it needs to be, add one to the goodPasswords
        if (letter == password[int(first)-1]):
            goodPasswords -= 1
            badPasswords += 1
            #if the letter is also in the first place it needs to be, subtract one from the goodPasswords and add one to the badPasswords
    else:
        badPasswords += 1
        #if the password does not follow the rules, it is added to badPasswords

print (goodPasswords)
print (badPasswords)
#both variables are printed