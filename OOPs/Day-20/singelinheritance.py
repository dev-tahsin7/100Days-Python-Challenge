# Singel Inheritance :

class Parent: # Parent Class
    def myFun1(self): # Parent Class Property
        print("Hello My Parent Class")

class Child(Parent): # Child Class # Inside Parameter we pass Parent Class
    def myFun2(self): # Child Class Property
        print("Hello My Child Class")

call = Child()
call.myFun1()
call.myFun2()