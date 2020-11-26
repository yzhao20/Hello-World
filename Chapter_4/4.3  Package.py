"""
1.  Create a python module: By definition, a module is basically a .py file which contains Python functions, global variables etc. 
"""
#!/usr/bin/env python3   # "#!" is called shebang or hashbang. Which is required in Unix or Unix-like envrionment, indicating which interpreter should process the file.
"""module.py - an example of Python module"""
__counter = 0   # A new variable called "__counter".

def suml(l):  # Define a function with an input called l
    global __counter # Use the global keyword to decalre this variable inside this function
    __counter += 1  # Plus 1
    sum = 0  # Initiate a sum variable with value 0
    for el in l:  # Get the sum of a list
        sum += el
    return sum # Output for this function

def prodl(l):
    global __counter  
    __counter += 1
    prod = 1
    for el in l:  # Get the product of a list
        prod *= el
    return prod

if __name__ == "__main__":   # "__name__" is a variable. If run a file directly, it's set to __main__ string; if a file is imported as a module, it's set to the file's name.
    print('I prefer to be a module, but I can do some tests for you.')
    l = [i+1 for i in range(5)]  # Create a list
    print(sum(l) == 15) # check if the output is equal to 15
    print(prodl(l) == 120)

    
"""
2. Use the module created in step 1.
"""
from module import suml, prodl   # Selective import

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeros))  # Use the function suml directly instead of module.suml
print(prodl(ones))



"""
3. Create a package, which has a number of modules and sub-packages too.
"""
from sys import path   # Selective import, and sys is another coomon built-in module.
path.append('C:\\Users\\yunfeng.zhao\\PycharmProjects\\PCPP\\Packages\\Extrapack_4_3_24.zip')  # Path is a list, so Path.append is used to add a specific package path list element. \
                                                                                               #Doulbe \ is used as we want to get a single backslash. The last element is a zip file but won't affect anything.
print(path)  # Print out this new list, "sys.path" is NOT allowed as this is a selective import.\
             # The list has Two category paths, one is about current working directory, and the other one is about Python software itself that including all standard libraries.

import extra.good.best.sigma as sig  # Sigma is a module, using alia makes it much easier
import extra.good.alpha as alp
from extra.iota import FunI  # Selective import, FunI is a specific function
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())
