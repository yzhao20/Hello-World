"""
1. Working with standard modules
"""
import math as M    # Import a module with alia name "M". The module has to be imported AS A WHOLE, i.e., using the "import module" instruction - "from module..." is NOT enough!
print(dir(M), len(dir(M)))  # dir() function returns an alphabetically sorted list containing all entities. 
print(type(dir(M))) # <class 'list'>

import math   # Pay attention to that we've imported the module as a whole, otherwise dir() won't work.
for name in dir(math):
    print(name, end = '\t')  # You may notice that some entities with _ at the top of the list.
    
import math  # We can use the dir() function directly in the Python console, without needing to write a seperate script.
dir(math)  # Write directly in console to get a list of all entities.


"""
2. Thress groups from the math module:
    Trigonometry 
    Exponential
    Ggeneral purpose
"""
from math import pi, radians, degrees, asin, sin, cos, tan  # Selective import
ad = 90    # Angle degree 
ar = radians(ad)  # Convert ad from degrees to radians
ad = degrees(ar)   # Convert ar from radians to degrees
print(ad == 90)   # Print out if they are equal to each other, same as below
print(ar == pi / 2)
print(sin(ar) / cos(ar) ==  tan(ar))   
print(asin(sin(ar)) == ar)


from math import e, exp, log   # Selective import
print(pow(e, 1) == exp(log(e))   # Pow(x,y) stands for x ** y, this function is a built-in function so no need to be imported. 
print(pow(2, 2) == exp(2 * log(2))  # log(x, b) stands for log of x base b. In particular, log10(x) is more precise than log(x, 10), so is log2(x).
print(log(e, e) == exp(0))


from math import ceil, floor, trunc  # Selective import
x = 1.4  
y = 2.6
print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
      

"""
3. Random module, and random, seed, randrange, randint functions.
"""
from random import random  # Two randoms: one module and one function. The function produces one float number [0.0,1.0)

for i in range(5):
    print(random())  # Random function without argument.

from random import random, seed  # Import random and seed functions
seed(50)  # The 50 argument is optional, if provided always get the same result. If not, it depends on current time.
for i in range(5):
    print(random())

from random import randrange, randint
print(randrange(1), end=' ')  # randrange(end), end is not included.
print(randrange(0, 1), end=' ')  # randrange(start, end), end is not included
print(randrange(0, 1, 1), end=' ')  # randrange(start, end, step), end is not included.
print(randint(0, 0)) # randint(left, right), BUT the right endpoint is included!
"""
4. choice, sample function to avoid repeatness.
"""
from random import choice, sample
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(l)) # Return one(default) value from population
print(sample(l, 5)) # Return a sample list (unordered) from population, and the # of elements shouldn't be greater than # of population.
print(sample(l, 10))
