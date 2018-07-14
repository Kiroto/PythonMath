# This will be the program to be ran
import math

class Mathify:
  # Don't need to construct anything yet.
  def __init__(self):
    pee = math.pi
    ee = math.e
  # Basic 6  
  # Ad as in Add
  def ad(self, x, y=0):
    return x + y
  
  # Mu as in Multiply
  def mu(self, x, y=1):
    return x * y
  
  # Ra as in Raise
  def ra(self, x, y=1):
    return math.pow(x, y)
  
  # Su as in Substract
  def su(self, x, y=0):
    return x - y
  
  # Di as in Divide
  def di(self, x, y=1):
    return x / y
  
  # Ro as in Root
  def ro(self, x, y=1):
    return math.pow(x, (1 / y))

  # Lo as in Logarithm
  def lo(self, x, y=10):
    if y == 10:
      return math.log10(x)
    return math.log(x, y)
  # Conversions
  # Degrees to radians
  def degtorad(self, x):
    return x * 180 / pee
  
  # Radians to degrees
  def radtodeg(self, x):
    return x * pee / 180
  
  # Trigonometric functions. All the input values should be converted to radians.
  # Adding a second parameter as True returns the arc functions.
  # Si as in Sine
  def si(self, x, y=False):
    x = degtorad(x)
    if y == True:
      return math.asin(x)
    return math.sin(x)
  
  # Co as in Cosine
  def co(self, x, y=False):
    x = degtorad(x)
    if y == True:
      return math.acos(x)
    return math.cos(x)
  
  # Ta as in Tangent
  def ta(self, x, y=False):
    x = degtorad(x)
    if y == True:
      return math.atan(x)
    return math.tan(x)
  
