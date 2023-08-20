a = input("Enter Your Number: ")
print(f"Multiplication Tabel of {a}")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")

print("Here we go..")

"""
Python Built in Exception Error types :
Link - https://docs.python.org/3/library/exceptions.html
"""

