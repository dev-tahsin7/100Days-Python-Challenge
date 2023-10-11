# Pure Function:

def my_function(a,b):
    name = f"My name is {a}. I am from {b}."
    return name

print(my_function("Tahsin","Bangladesh"))

# Impure Function: 

my_list = [] # create a blank list

def my_impure_function(x):
    my_list.append(x)

my_impure_function("Tahsin")
print(my_list) 

# Lamda:

lam_fun = lambda y: y*y*y
print(lam_fun(3)) 

# Lamda is the easy way to use function and use expression.
# By using lamda you can create anonymous function
# shortcut way to use function in single line 
# When we need to pass function as a arg then we use lamda

def new_lamda_use(f, value):
    return 6+ f(value)

print(new_lamda_use(lam_fun,3))