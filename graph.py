# I affirm that I have carried out my academic endeavors with full academic honesty.
# Rathika Nair 
# Make sure to add an appropriate header comment.

import turtle


def draw_axis():
  turtle.speed(5)
  turtle.penup()
  turtle.goto(500,-300)
  turtle.pendown()
  turtle.width(2)
  turtle.forward(-1000)
  turtle.left(90)
  turtle.forward(700)



def label():
  turtle.penup()
  turtle.goto(-700, 0)
  turtle.pendown()
  turtle.write("Spectral Type", font=("Verdana", 12, "bold"))

  turtle.penup()
  turtle.goto(0, -360)
  turtle.pendown()
  turtle.write("Semi-major axis [au]", font=("Verdana", 12, "bold"))



def y_tickmarks():
  turtle.right(90)
  
  y = -220
  for i in range(3):
    turtle.penup()
    turtle.goto(-520, y)
    turtle.pendown()
    turtle.forward(40)
    y = y + 220

  turtle.penup()
  turtle.goto(-550, -220)
  turtle.pendown()
  turtle.write("F", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(-550, 0)
  turtle.pendown()
  turtle.write("G", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(-550, 220)
  turtle.pendown()
  turtle.write("K", font=("Verdana", 15, "bold"))
  
  

def x_tickmarks():
  turtle.left(90)
  
  x = -360
  for i in range(7):
    turtle.penup()
    turtle.goto(x, -320)
    turtle.pendown()
    turtle.forward(40)
    x = x + 120

  turtle.penup()
  turtle.goto(-380, -340)
  turtle.pendown()
  turtle.write("0.1", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(-260, -340)
  turtle.pendown()
  turtle.write("0.2", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(-140, -340)
  turtle.pendown()
  turtle.write("0.5", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(-20, -340)
  turtle.pendown()
  turtle.write("1.0", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(100, -340)
  turtle.pendown()
  turtle.write("2.0", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(220, -340)
  turtle.pendown()
  turtle.write("3.0", font=("Verdana", 15, "bold"))

  turtle.penup()
  turtle.goto(340, -340)
  turtle.pendown()
  turtle.write("4.0", font=("Verdana", 15, "bold"))



def draw_planets():
  turtle.penup()
  turtle.goto(-140, 0)
  turtle.pendown()
  turtle.fillcolor("yellow")
  turtle.begin_fill()
  turtle.circle(4.77*5)
  turtle.end_fill()
  

  turtle.penup()
  turtle.goto(220, 220)
  turtle.pendown()
  turtle.fillcolor("orange")
  turtle.begin_fill()
  turtle.circle(2.81*5)
  turtle.end_fill()
  

  turtle.penup()
  turtle.goto(-20, 0)
  turtle.pendown()
  turtle.fillcolor("yellow")
  turtle.begin_fill()
  turtle.circle(3.29*5)
  turtle.end_fill()
  

  turtle.penup()
  turtle.goto(-170, 0)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(3.57*5)
  turtle.end_fill()

  turtle.penup()
  turtle.goto(-150, 0)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(3.93*5)
  turtle.end_fill()

  turtle.penup()
  turtle.goto(-40, 0)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(3.93*5)
  turtle.end_fill()

  turtle.penup()
  turtle.goto(-20, 0)
  turtle.pendown()
  turtle.fillcolor("blue")
  turtle.begin_fill()
  turtle.circle(1*5)
  turtle.end_fill()

  turtle.goto(-20, 5)
  turtle.write("Earth", font =("Verdana", 10))



  

def graph():
  draw_axis()
  label()
  y_tickmarks()
  x_tickmarks()
  draw_planets()
  turtle.hideturtle()
  
  turtle.done()