#Isha Chaudhuri, 07/03
goodPasswords = 0
badPasswords = 0


f = open("input.txt")

for item in f.readlines():
    rule, pw = item.split(": ", maxsplit=1)
    minmax, symbol = rule.split(" ", maxsplit=1)
    lower, upper = (int(x) for x in minmax.split("-", maxsplit = 1))

    numSymbols = pw.count(symbol)

    if (lower <= numSymbols) and (numSymbols <= upper):
        goodPasswords += 1

    if (pw[lower - 1] is symbol) ^ (pw[upper - 1] is symbol):
        badPasswords += 1


print(goodPasswords)


    
