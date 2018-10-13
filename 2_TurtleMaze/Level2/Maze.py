from Tile import Tile, TileType, move
from enum import IntEnum

class Direction(IntEnum):
  EAST = 0
  NORTH = 90
  WEST = 180
  SOUTH = 270

class Maze():
  def __init__(self, tileSize):
    self.grid = None
    self.start = None
    self.finish = None
    self.rows = None
    self.cols = None
    self.tileSize = tileSize

  def loadMaze(self, filename):
    rawMaze = []
    
    with open(filename, 'r') as f:
      for line in f:
        rawMaze.append(list(line.rstrip('\n')))

    self.rows = len(rawMaze)
    self.cols = max([len(row) for row in rawMaze])
    
    self.grid = [[Tile(x, y) for y in range(self.rows)] for x in range(self.cols)]

    for y, row in enumerate(rawMaze):
      for x, cell in enumerate(row):
        tile = self.grid[x][y]
        if cell == '+':
          tile.setType(TileType.WALL)
        elif cell == 'S':
          tile.setType(TileType.START)
          self.start = tile
        elif cell == 'F':
          tile.setType(TileType.FINISH)
          self.finish = tile

  def drawMaze(self, pen):
    if self.grid is None:
      print('no maze loaded')
      return False
    
    for x, col in enumerate(self.grid):
      for y, cell in enumerate(col):
        tile = self.grid[x][y]
        tile.draw(pen, self.tileSize)

  def drawPathFromStart(self, pen, headings):
    move(pen, self.__getCentralX(self.start), self.__getCentralY(self.start))
    self.drawPath(pen, headings)

  def drawPath(self, pen, headings):
    """draws a turtle path based on an array of headings"""
    for heading in headings:
      pen.setheading(heading)
      pen.forward(self.tileSize)


  def __getCentralX(self, tile):
    return tile.x * self.tileSize + self.tileSize / 2
  
  def __getCentralY(self, tile):
    return tile.y * self.tileSize - self.tileSize / 2