# Use of Constructor 

class Person:
    def __init__(self,n,a,c):
        self.name = n 
        self.age = a 
        self.country = c 

    def info(self):
        print(f"My name is {self.name}. I am from {self.country}. I am {self.age} years old")

x = Person("Tahsin",18,"Bangladesh")
x.info()
y = Person("Bayazid", 19 , "Japan")
y.info()