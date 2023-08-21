"""
print this :
#
# #
# # #
# # # #
"""

# Solution:

for i in range(4):
    for j in range(i+1):
        print("#", end=" ")
    print()

"""
# # # #
# # #
# #
#
"""

# Solution:

for i in range(4,0,-1):
    for j in range(0,i):
        print("#", end=" ")
    print()

# Swaping two element in List 

# Solution:

x = [1,2,4,3,5,6]
# We will swip 4 & 3
y = x[2]
x[2] = x[3]
x[3] = y
print(x)
