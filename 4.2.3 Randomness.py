"""
1. Random module, and random, seed, randrange, randint functions.

"""
from random import random    # The first random is a module, and the second one is a function that produces a Float number coming from [0.0, 1.0), NOT including right end point 1.0
for i in range(5):  # Will produce five pseudorandom values
    print(random())     # Random here is a function without argument, and their values are determined by the current (rather unpredictable) seed value, you can't simply guess them.


from random import random, seed   # Import the sedd function this time
seed(50)   # Two cases here: seed() which sets the seed with the current time, seed(i) which sets the seed with the integer value i. In the latter case, we get the SAME values every time.
for i in range(5):
    print(random())
