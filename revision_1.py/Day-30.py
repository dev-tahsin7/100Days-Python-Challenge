def sq(x):
    return x*x
print(sq(2))

li = [1,2,3,4]
newL =list(map(sq, li)) # Map Function
print(newL)

""" 
map() function returns a map object(which is an iterator) 
of the results after applying the given function to each 
item of a given iterable (list, tuple etc.)
Python map() Function

Syntax:
map(fun, iter)

Parameters:
    fun: It is a function to which map passes each element 
    of given iterable.
    iter: It is iterable which is to be mapped.

NOTE: You can pass one or more iterable to the map() function.
Returns:

Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 

 NOTE : The returned value from map() (map object) then can be 
 passed to functions like list() (to create a list), set() 
 (to create a set) . 

"""