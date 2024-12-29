'''Q5. Write a Python program that takes a number as input and checks if it is a 3-digit
number.'''

num=int(input("Enter Number : "))

num_of_digits=0

while(num!=0):
    num=num//10
    num_of_digits +=1

if (num_of_digits==3): 
    print("Its a three digit number")
else: 
    print("Not a three digit number")