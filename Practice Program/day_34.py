# 9. Find Factoeial of a number :
num = int(input("Enter Your Numer: "))
factorial = 1

if num < 0 :
    print("Factorial doesn't exsit")

if num == 0 : 
    print("Factorial is 1")

if num > 0:
    for i in range(1,num+1):
        factorial = factorial * i

print(f"Factorial of {num} is {factorial}")

# 10. Fibonacci Sequence : 
num = int(input("Enter Your Number: "))
a = 0 
b = 1 

if num == 1 :
    print(a)

else: 
    print(a)
    print(b)
    for i in range(1, num+1):
        c = a + b
        a = b
        b = c 
        print(c)

# 11. If the number is Armstrong or not : 
num = int(input("Enter Your Number: "))

sum = 0 
temp = num 

while temp > 0 :
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube 
    temp = temp // 10  

if sum == num :
    print("It's an Armstrong Number")
else:
    print("It's not an Armstrong Number")

# Explenation in my hand note ! 

# 12. Decimal to Binary , Octal & Hexadecimal :
deci = int(input("Enter Your Number: "))

print(f"Here is the binary , octal & hexadecimal of {deci}: ")
print(bin(deci), "in binary")
print(oct(deci), "in octal")
print(hex(deci), "in hexadecimal")

# 13. Find ASCII value of Character:

char = "T"

print(f"The ASCII value of {char} is {ord(char)}")