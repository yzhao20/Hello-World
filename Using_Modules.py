"""
1.   Import a module
"""
import math   # Importa math module, whenenver we want to use any entity in that module, just follow the math.entity syntax.
print(math.pi)   # Print out one math entity
print(math.sin(math.pi/2)) # Same as above, but remember to qualify the entity before using it
print(math.e)
print(math.log(math.e))


"""
2.   Selective Import
"""
from math import pi, sin  # Selective import. I.e. from math module, only import two entities called pi and sin (this is a function).
print(sin(pi / 2))  # Print out sin(pi/2), where sin function, pi constant are both from math module.
pi = 3.14  # Redefine pi 
def sin(x):  # Redefine sin function
    if 2 * x == pi:    # If condition is met, where pi is 3.14 rather than pi in the math module
        return 0.9999  # Output 
    else: # Else condition
        return None
print(sin(pi / 2))  # Call the sin function that is NOT the one in math modeule, and print out the return value.



"""
3.   Import all entities
"""
from math import *  # This is a more aggressive form to import all entities. Convenient but UNSAFE simply because it may not able to avoid name conflicts.



"""
4.   Module alias
"""
import math as M  # Want to use a short, consice name for that particular module. Once executed, the original module name is no longer valid.



"""
5.   Module Entity alias
"""
from math import pi as P, sin as S, e as E   # From math module, only import pi, sin and e with alias seperately
print(P)  # Print out pi
print(S(P/2))  # Print out sin(pi/2)
print(math.log(E)) # Error message as math.log is NOT imported.


