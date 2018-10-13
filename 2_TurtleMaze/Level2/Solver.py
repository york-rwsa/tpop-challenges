from Maze import Direction
from Tile import TileType

class Solver():
  def __init__(self, maze):
    self.maze = maze
  
  def simpleSolution(self):
    x = self.maze.start.x
    y = self.maze.start.y
    visited = []
    moves = []

    while(self.maze.grid[x][y].type != TileType.FINISH):
      visited.append(self.maze.grid[x][y])
      heading = self.getMove(x, y, visited)
      
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
    
    return moves
  

  def getMove(self, x, y, visited):
    tiles = {direction: self.__getAdjacent(x, y, direction) for direction in Direction}
    
    for direction in Direction:
      tile = tiles[direction]
      if tile is not None and tile.type != TileType.WALL and tile not in visited:
        return direction
    else:
      return None

  def __getAdjacent(self, x, y, direction):
    if direction == Direction.WEST:
      return self.maze.grid[x - 1][y] if x - 1 > 0 else None
    elif direction == Direction.SOUTH:
      return self.maze.grid[x][y - 1] if y - 1 > 0 else None
    elif direction == Direction.EAST:
      return self.maze.grid[x + 1][y] if x + 1 < self.maze.cols else None
    elif direction == Direction.NORTH:
      return self.maze.grid[x][y + 1] if y + 1 < self.maze.rows else None

  def __reverseDirection(self, direction):
    if direction == Direction.WEST:
      return Direction.EAST
    elif direction == Direction.EAST:
      return Direction.WEST
    elif direction == Direction.SOUTH:
      return Direction.NORTH
    elif direction == Direction.NORTH:
      return Direction.SOUTH