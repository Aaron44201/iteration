#Aaron Bentley
#task 3
#17/10/14
import pdb
pdb.set_trace()
total = 0
count = 0
number = 1
while number > 0:
    number = int(input("enter a number "))
    total = total + number
    count = count + 1  
count = count - 1  
answer = total/count
print(answer)
