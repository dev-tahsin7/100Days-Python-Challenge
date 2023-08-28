# Create a class
class myClass:
    x = 7 # here is x class property 

# how to get access of x ?
# Creating an object and get access of x
a1 = myClass()
# print(a1.x)

# Call function by object 

class myFun:
    def myFunction(self):
        print("Hello World")

m1 = myFun()
print(m1.myFunction())