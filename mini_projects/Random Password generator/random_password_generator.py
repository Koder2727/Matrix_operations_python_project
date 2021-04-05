#Program to generate a random password
#importing the random library

import random
import string

#Taking the length of the password
length=int(input("Enter the length of your password you want to generate"))
print("It will be a random mixture of characters and numbers")
print("Enter the number of integers")

#runnig the while loop till correct input is given
while(True):
    intno=int(input())
    if(intno>length):
        print("numbers more than the length, Try again")
    else:
        print("Ok")
        break

#creating a list of words and numbers to store the random values generated  by the system
password=list()

#generate the random int and add them to the list
for i in range(intno):
    k=random.randint(0,9)
    password.append(k)

#generate the random str and add them to the list
for i in range(length-intno):
    k=random.choice(string.ascii_letters)
    password.append(k)

#function to shuffle the string
def shuffle(password):
    random.shuffle(password)
    final=""
    for ele in password:
        final=final+str(ele)
    return(final)

#printing the password   
password=shuffle(password)
print("The password is ",password)    