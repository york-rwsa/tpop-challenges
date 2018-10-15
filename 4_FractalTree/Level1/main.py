import turtle

def drawBranch(pen, length, multiplier, angle, stop):
  if length < stop:
    pen.color('green')
    pen.forward(length)
    pen.color('black')
    return
  else:
    pen.forward(length)

  coors = (pen.xcor(), pen.ycor())
  heading = pen.heading()


  pen.right(angle)
  drawBranch(pen, length*multiplier, multiplier, angle, stop)
  
  pen.penup()
  pen.goto(coors[0], coors[1])
  pen.pendown()
  pen.setheading(heading)

  pen.left(angle)
  drawBranch(pen, length*multiplier, multiplier, angle, stop)

window = turtle.Screen()
pen = turtle.Turtle()
pen.width(3)
pen.setheading(90)
drawBranch(pen, 60, 0.7, 33, 10)

pen.penup()
pen.goto(0, 0)
window.exitonclick()