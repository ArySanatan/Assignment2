'''Q4. Write a Python program to check the number of digits of user input using a loop.
'''

num=int(input("Enter Number : "))

num_of_digits=0

while(num!=0):
    num=num//10
    num_of_digits +=1
    
print("Number of digits = ",num_of_digits)