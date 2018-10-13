from enum import Enum

class TileType(Enum):
  EMPTY = 0
  WALL = 1
  START = 2
  FINISH = 3

class Tile():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.visited = False
    self.type = TileType.EMPTY
  
  def setType(self, tileType):
    self.type = tileType

  def draw(self, pen, tileSize):
    if self.type == TileType.WALL:
      pen.begin_fill()
      drawRect(pen, self.x*tileSize, self.y*tileSize, tileSize, tileSize)
      pen.end_fill()

  def __repr__(self):
    return '({}, {}) of {}'.format(self.x, self.y, self.type)


def move(pen, x, y):  
  pen.penup()
  pen.goto(x, y)
  pen.pendown()

def drawRect(pen, startx, starty, width, height):
  """Draw a rectangle with the top left corner at (startx, starty)"""
  move(pen, startx, starty)

  # start by drawing top edge (east)
  pen.setheading(0)
  pen.forward(width)
  
  # right edge (south)
  pen.setheading(270)
  pen.forward(height)
  
  # bottom edge (west)
  pen.setheading(180)
  pen.forward(width)
  
  # left edge (north)
  pen.setheading(90)
  pen.forward(height)