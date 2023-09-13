# Regular Expression 
import re
x = open('check.txt')

y = re.findall("Lion", x)
print(y)

'''
for x in file:
    if re.search( '(waken|open)ed', x ):
        print(x) '''