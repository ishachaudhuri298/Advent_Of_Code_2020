#Isha Chaudhuri, 07/16

goodPasswords = 0
badPasswords = 0
#creating a variable to store the number of good and bad passwords 

f = open("input.txt")
#opening the input file

for item in f.readlines():
    #for loop that reads through each line of the input file 
    [number, letter, password] = item.split()
    #splits each line in the input into its specific number, letter, and password
    for item in number:
        [lower,upper] = item.split("-")
        #splits each rule for the numbers into the lower number and the upper number
    totalNumberOfLetters = password.count(letter)
    #counts how many letters are in each password and assigns to a variable
    if (lower <= totalNumberOfLetters) and ( upper >= totalNumberOfLetters):
        goodPasswords += 1
    else:
        badPasswords += 1

print (goodPasswords)
print (badPasswords)

   