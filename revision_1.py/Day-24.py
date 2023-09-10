name = ['Tahsin','bayazid','Mahi']

for x in name:
    if x == 'bayazid': 
        continue
    # print(x)
"""
# While loop
x = True
while x:
    xy = input("Your Name: ")
    if xy == "Tasu":
        x = False # We can also use "break" keyword """

# List Comprehension

name = ['Tahsin','Tasu','Mahi','Tanjid','Bayazid']
newList = [x for x in name if 'T' in x]
print(newList)