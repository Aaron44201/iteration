#Aaron Bentley
#10/10/14
#ascii

import random
import string

charecter_num = int(input("enter the lenth of password: "))
list1 = ""
while charecter_num > 0:
    password = random.choice(string.ascii_letters)
    list1 = list1 + password
    charecter_num = charecter_num - 1
print("password {0}".format (list1))

              
