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
  
  def solveMaze(self, pen):
    move(pen, self.__getCentralX(self.start), self.__getCentralY(self.start))

    x = self.start.x
    y = self.start.y
    moves = []

    while(self.grid[x][y].type != TileType.FINISH):
      heading = self.getMove(x, y)
      
      if heading is None:
        # backtrack
        if len(moves) == 0:
          print('No Solution')
          break
        
        prevMove = moves.pop()
        heading = self.__reverseDirection(prevMove)
      else:
        moves.append(heading)
      
      if heading == Direction.NORTH:
        y = y + 1
      elif heading == Direction.SOUTH:
        y = y - 1
      elif heading == Direction.EAST:
        x = x + 1
      elif heading == Direction.WEST:
        x = x - 1
      
      pen.setheading(heading)
      pen.forward(self.tileSize)

      self.grid[x][y].visited = True

    print(self.start)
  

  def getMove(self, x, y):
    tiles = {direction: self.__getAdjacent(x, y, direction) for direction in Direction}
    
    for direction in Direction:
      tile = tiles[direction]
      if tile is not None and tile.type != TileType.WALL and tile.visited == False:
        return direction
    else:
      return None

  def __getCentralX(self, tile):
    return tile.x * self.tileSize + self.tileSize / 2
  
  def __getCentralY(self, tile):
    return tile.y * self.tileSize - self.tileSize / 2

  def __getAdjacent(self, x, y, direction):
    if direction == Direction.WEST:
      return self.grid[x - 1][y] if x - 1 > 0 else None
    elif direction == Direction.SOUTH:
      return self.grid[x][y - 1] if y - 1 > 0 else None
    elif direction == Direction.EAST:
      return self.grid[x + 1][y] if x + 1 < self.cols else None
    elif direction == Direction.NORTH:
      return self.grid[x][y + 1] if y + 1 < self.rows else None

  def __reverseDirection(self, direction):
    if direction == Direction.WEST:
      return Direction.EAST
    elif direction == Direction.EAST:
      return Direction.WEST
    elif direction == Direction.SOUTH:
      return Direction.NORTH
    elif direction == Direction.NORTH:
      return Direction.SOUTH