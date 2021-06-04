import math

class Rectangle:
  width = 0
  height = 0

  def __init__(self, wid, hei):
    self.width = wid
    self.height = hei

  def get_width(self):
    return self.width
  
  def get_height(self):
    return self.height

  def set_width(self, newWidth):
    self.width = newWidth

  def set_height(self, newHeight):
    self.height = newHeight
  
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    picture = ''
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'

    for i in range(self.height):
      for j in range(self.width):
        picture += '*'
      if i != self.height:
        picture += '\n'

    return picture
  
  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

  def get_amount_inside(self, shape):
    widthRatio = math.floor(self.get_width() / shape.get_width())
    heightRatio = math.floor(self.get_height() / shape.get_height())
    return widthRatio * heightRatio

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
  
  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side

  def set_width(self, new_width):
    self.width = new_width
    self.height = new_width
    
  def set_height(self, new_height):
    self.width = new_height
    self.height = new_height

  def __str__(self):
    return 'Square(side=' + str(self.width) + ')'
  

