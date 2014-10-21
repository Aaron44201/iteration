#Aaron Bentley
#task 3
#20/10/14
total = 0
count = 0
number = 1
while number > 0:
    number = int(input("enter a number "))
    if number > 0:
        total = total + number
        count = count + 1  
answer = total/count
print(answer)
