"""
1. Random module, and random, seed, randrange, randint functions.
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
2. choice, sample function to avoid repeatness.
"""
from random import choice, sample
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(l)) # Return one(default) value from population
print(sample(l, 5)) # Return a sample list (unordered) from population, and the # of elements shouldn't be greater than # of population.
print(sample(l, 10))


