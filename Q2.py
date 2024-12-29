'''Q2.  Write a Python program that checks palindrome.
(e.g. {abba, 12321, and abbabba} is a palindrome but {bac, 1302, 1212} are not)'''

input_str=input("Enter a String : ")

for s in input_str:
    if input_str==input_str[::-1]:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")
    break