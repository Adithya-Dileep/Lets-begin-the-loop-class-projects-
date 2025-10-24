import turtle
# Create a turtle object
pen = turtle.Turtle()
pen.speed(0) # Set the drawing speed to the fastest
# Set initial parameters
side_length = 5
angle = 90
num_iterations = 250
# Draw the square spiral
for _ in range(num_iterations):
    pen.forward(side_length)
    pen.right(angle)
    side_length += 3 # Increase the side length for the next segment
# Keep the window open until closed manually
turtle.done()