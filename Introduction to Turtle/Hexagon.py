import turtle
screen = turtle.Screen()
screen.bgcolor('Green')
screen.setup(500,500)
board = turtle.Turtle()
side = 6
length = 100
angle = 360/side
for i in range(side):
    board.forward(length)
    board.right(angle)
turtle.done()    