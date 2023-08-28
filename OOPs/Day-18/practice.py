class Person:
    name = "Tahsin"
    work = "Student"
    age = 19 
    def info(self):
        print(f"{self.name} is a {self.work}. He is {self.age}")

a = Person()
a.info()

b = Person()
b.name = "Mahi"
b.age = 18
b.info() 