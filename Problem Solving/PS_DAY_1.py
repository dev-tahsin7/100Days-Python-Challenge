"""
print this :
#
# #
# # #
# # # #
"""

# Solution:

# for i in range(4):
#     for j in range(i+1):
#         print("#", end=" ")
    # print()

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