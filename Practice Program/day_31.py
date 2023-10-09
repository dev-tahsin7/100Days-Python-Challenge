# 1. Area of Triangle :
height = int(input("Input Height of Triangle: "))
base = int(input("Input Height of Triangle: "))

result = 0.5 * (base*height)
print(f"Your area of Triangle is {result}")

# 2. Swaip two variable 
x = 12
y = 13
#Solution-1
tem = x 
x = y
y = tem

#Solution-2
x,y = y,x
print(y)

# 3. Killometers to miles converter:
km = float(input("Enter your killometers: "))
miles = km * 0.621271
print(f"Your convert result {miles}")

# 4. Check if a number positive, negative or zero
num = float(input("Enter your number: "))

if num > 0 :
    print("It's a positive number")
elif num == 0:
    print("It's Zero")
else:
    print("It's a negative number")

# 5. Check leap year:
year = int(input("Enter your year: "))

if year % 400 == 0 and year % 100 == 0:
    print(f"{year} is a leap year")

elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")
