# 6. Check Leargest Number:
num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your 2nd Number: "))
num3 = int(input("Enter Your 3rd Number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the leargest number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the leargest number")
else:
    print(f"{num3} is the leargest number")

# 7. Check Prime Number
x = int(input("Enter Your Number: "))
if x == 1:
    print("It's not a prime number")

for i in range(2,x):
    if x%i == 0:
        print("It's not a prime number")
        break
    else:
        print("It's a prime Number")

# 8. celsius to fahrenheit:
cele = float(input("Entre today temp: "))
fah = (cele * 9/5) + 32
print(f"Your temp in Fahrenheit {fah}F")
