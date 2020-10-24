"""
Python prefers to use "try... except" statement to handle errors rather than "if... else" statments.
"""
try:  # This is the prefer approach.
  x = int(input("> "))
  y = 1 / x
  print(y)
except ValueError:  # ValueError is a builtins.
  print("Please enter an integer value.")
except ZeroDivisionError:   # ZeroDivisionError is a builtins.
  print("Please enter an non-zero value")
except:  # General exception besides the cases above.
  print("Oh, dear.")
print("The END.")  # This is outside the try-except statement.
