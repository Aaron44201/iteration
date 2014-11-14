number = int(input("please enter an integer "))
for count in range (0,12):
    total = count*number
    print("{0:2} * {1} = {2:3}".format (count,number,total))
