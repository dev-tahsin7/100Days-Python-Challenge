# Try to develop a calculator
class Calcu:
    def __init__(self, n1 , n2 ):
        self.num1 = n1
        self.num2 = n2 

    def calculation(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")

a = Calcu(int(input("Enter First Number: ")), int(input("Enter 2nd Number: ")))
a.calculation()