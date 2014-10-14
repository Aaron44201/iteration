# program to prompt for 8 numbers and report the total to the user
total=0
for count in range (1,9):
    number = int(input("enter number {0} please: ".format (count)))
    total = total + number
print('The total is {0}'.format(total))


