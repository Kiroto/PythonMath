# This will be the program to be ran
import Math

class Mathify:
  # Don't need to construct anything yet.
  def __init__(self):
    pass
  # Basic 6  
  # Ad as in Add
  def ad(self, x, y=0):
    return x + y
  
  # Mu as in Multiply
  def mu(self, x, y=1):
    return x * y
  
  # Ra as in Raise
  def ra(self, x, y=1):
    return x ** y
  
  # Su as in Substract
  def su(self, x, y=0):
    return x - y
  
  # Di as in Divide
  def di(self, x, y=1):
    return x / y
  
  # Ro as in Root
  def ro(self, x, y=1):
    return x ** (1 / y)
