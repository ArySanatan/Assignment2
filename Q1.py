'''Q1. Write a Python program that takes input as a string and prints the reverse of it using a
loop.'''

input_str=input("Enter a String : ")

i=1
rev_str=""
while(i<=len(input_str)):
    remainder=input_str[-1*i]
    rev_str=rev_str + remainder 
    i=i+1
    
print("Reversed String = ", rev_str)