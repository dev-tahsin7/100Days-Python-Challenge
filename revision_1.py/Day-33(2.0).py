# Map:
def my_fun(x):
    return x * 2

my_list =[1,2,3,4,5]
result = map(my_fun, my_list) #map(function, iterable)
# print(list(result))

# Filter:
def my_new_fun(x):
    return x%3 == 0

my_new_list = [1,2,3,6,9,10,12,15,17]
fil = filter(my_new_fun,my_new_list) #filter(function,iterable)
print(list(fil))

# we can also use lamda is map,filter !! 