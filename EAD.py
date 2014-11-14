number = 0
total = 0
while -1 < number or number > -1 :
    number = int(input("Please enter a number: "))
    total = total + (number*number)
total = total-1
print("The total is  {0}".format (total))
