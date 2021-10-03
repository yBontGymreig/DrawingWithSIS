from random import randint
from turtle import *
'''
forward(50) #travel 50 units forward
left(120) #turn left 120 degrees
forward(50)
left(120)
forward(50)
left(120)

penup()
forward(100)
pendown()

forward(50)

left(120)
forward(50)
left(120)
forward(50)
left(120)

print("X position is now: ", pos()[0])
print("Y position is now: ", pos()[1])
'''

def rainbow_color_cycle(turtle, speed_change = 1):
  color = turtle.pencolor()
  red = color[0]
  green = color[1]
  blue = color[2]
  if red == 255 and green < 255 and blue == 0:
    green += speed_change
  elif green == 255 and red > 0:
    red -= speed_change
  elif green == 255 and blue < 255:
    blue += speed_change
  elif blue == 255 and green > 0:
    green -= speed_change
  elif blue == 255 and red < 255:
    red += speed_change
  elif red == 255 and blue > 0:
    blue -= speed_change
  turtle.pencolor(red, green, blue)

def rainbow_color_cycle2(turtle, speed_change = 1):
  color = turtle.pencolor()
  red = color[0]
  green = color[1]
  blue = color[2]
  #if moving from red to green make more green and less red
  if red > 0 and green < 255 and blue == 0:
    green += speed_change
    if green > 255:
      green = 255
    red = 255 - green
    print(1, red, green)
  # elif moving from green to blue, make more blue and less green
  elif red == 0 and green > 0 and blue < 255:
    blue += speed_change
    if blue > 255: blue = 255
    green = 255 - blue
  
  # elif moving from blue to red, make more red and less blue
  elif green == 0 and blue > 0 and red < 255:
    red += speed_change
    if red > 255: red = 255
    blue = 255 - red
  turtle.pencolor(red, green, blue)


dave = Turtle()
dave.pencolor((255,0,0))
dave.speed(100)
angle = 0
y_pos = 0
x_pos = 0
while True:
  dave.goto(x_pos, y_pos)
  dave.pendown()
  dave.forward(100)
  dave.penup()
  y_pos += 1
  rainbow_color_cycle(dave, 5)
  
'''
Below I have written some useful commands you can use and hack/tweak. They won't be executed because in Python if you put 3 quote marks around a section, it becomes a multi-line comment.
#getting a random integer(whole number)
left(randint(1,179))

#finding out the position using pos().
current_position = pos()

#The position is a tuple format for co-ordinates: (0.0, 100.0). You can access the first part ith [0] and the second part with [1]
x_pos = pos()[0]
y_pos = pos()[1]

penup()
pendown()
color("Blue")
color(255,0,0)

# Drawing a triangle using a while loop iteration:
# first setting variables
num_sides = 3
angle = 120
length = 100
sides_drawn = 0
keep_going = True

while keep_going:
  if sides_drawn < num_sides:
    forward(length)
    right(angle)
  else:
    keep_going = False



#iteration
for i in range(10):
  #do whatever is in here
  #10 times
  print("Loop number", i)

'''