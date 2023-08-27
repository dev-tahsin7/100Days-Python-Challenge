# File Handling 

# Syntax :
# f = open("ve.txt", "r") 
# Here 1st para is filenaem 
# 2nd para is mode 
"""
There is 4 diffrent mode in Python

"r" - Read the file 
"a" - Appending the file
"x" - Create a specified file
"w" - Write a file

and also there two mode 
"t" - Text Mode
"b" - Binary Mode
"""

# Read a File
# f = open("main.txt", "rt")
# print(f.read())
# we can also read a file line by line
# print(f.readline())
# f.close 

# Write and Append
# f = open("main.txt", "a") # Appending
# print(f.write("Hello People"))
# f.close

# f = open("main.txt", "r")
# print(f.read())

# Append will add text in last 

f = open("main.txt" , "w")
print(f.write("Hello BAD Boys"))
f.close

f = open("main.txt" , "r")
print(f.read())

# w - write will overwrite text file

# Create a file 

f = open("check.txt" , "x") # that will create a empty file

