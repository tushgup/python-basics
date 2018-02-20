#Simple Class
class Rectangle:
  l = 0
  b = 0
  def __init__(self, l = 4, b = 5):
    self.l = l
    self.b = b
  def area(self):
    area = self.l * self.b
    return area

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
rect = Rectangle(length, breadth)
print("Area is: " + str(rect.area()))
print("Using default values")
rect1 = Rectangle()
print("Area is: " + str(rect1.area()))
