class X:
    def myFun(self,a):
        print("Hello Bro")

class X1(X):
    def myFun(self,a):
        print("Hey Bro")
        super().myFun(10)

class X2(X1):
    def myFun(self,a):
        print("Hi Bro")

class_call = X2()
class_call.myFun(10)
