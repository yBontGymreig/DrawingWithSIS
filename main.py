from random import randint
from turtle import *


def rainbow_color_cycle(turtle, speed_change = 1):
  color = turtle.pencolor()
  red = color[0]
  green = color[1]
  blue = color[2]
  
  
  turtle.pencolor(red, green, blue)
  print(turtle.color())

#create a turtle
dave = Turtle()

#start at red
dave.pencolor((255,0,0))
dave.speed(100)
angle = 0
y_pos = 0
x_pos = 0

#keep drawing lines and moving up
while True:
  dave.goto(x_pos, y_pos)
  dave.pendown()
  dave.forward(100)
  dave.penup()
  y_pos += 1
  rainbow_color_cycle(dave, 5)
