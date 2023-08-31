# Multilevel Inheritance

class Parent: # Parent Class
    def myFunction(self): # Parent Class Property
        print("Main Parent Class")

class Sub_Parent(Parent): # Sub Parent Class 
    def myFunction1(self): #Sub Parent Class Property
        print("Sub Parent Class")

class child(Sub_Parent): # Child Class
    def myFunction2(self): # Child Class Property
        print("Child Class of Main and Sub Parent Class")

# Create a object for child class
o1 = child()
o1.myFunction()
o1.myFunction1()
o1.myFunction2()  # Now we can access any of class property by using child class


""" There is also more three types of Inheritance
one is Multiple Inheritance, hierarchical inheritnce another one is hybrid Inheritance.

Now what is Multiple Inheritance ?
Multiple Inheritance is where is multiple Parent class inherit in a child class

Now what is Hierarchical Inheritance?
There is only one parent class but lots of child classess

Now what is Hybird Inheritance?
It's actually combination of many inheritance
 """