import random
guessed = False
number = random.randint(1,100)
noofturns = 0
while guessed == False:
    noofturns = noofturns+ 1
    userguess = int(input("Enter your guess for the number: "))
    if userguess == number:
        guessed = True
    elif userguess > number:
        print("the number you guessed is to high")
    else:
        print("The number you guessed is to low")
print("You took {0} turns to guess the number".format (noofturns))
print("The number was {0}".format (number))
