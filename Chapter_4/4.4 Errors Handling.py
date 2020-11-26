"""
Python prefers to use "try... except" statement to handle errors rather than "if... else" flow control.
"""
try:  # This is the prefer approach.
  x = int(input("> "))   # Integer conversion could get ValueError.
  y = 1 / x    # Division could get an ZeroDivisionError.
  print(y)
except ValueError:  # ValueError is a builtins, the order of exception DOES matter.
  print("Please enter an integer value.")
except ZeroDivisionError:   # ZeroDivisionError is a builtins.
  print("Please enter an non-zero value")
except:  # General exception besides the cases above.
  print("Oh, dear.")
print("The END.")  # This is outside the try-except statement.
