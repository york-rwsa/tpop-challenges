import turtle
from time import sleep
from Maze import Maze
from Solver import Solver

window = turtle.Screen()
mazePen = turtle.Turtle()
mazePen.speed(0)

maze = Maze(15)
maze.loadMaze('maze.txt')

delay = turtle.delay()
tracer = turtle.tracer()

turtle.tracer(0, 0)
maze.drawMaze(mazePen)
turtle.update()
turtle.tracer(tracer, delay)

solPen = turtle.Turtle()
solPen.color('red', 'green')
solver = Solver(maze)
headings = solver.simpleSolution()
maze.drawPathFromStart(solPen, headings)

window.exitonclick()