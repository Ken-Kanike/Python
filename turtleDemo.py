from turtle import *
import colorsys

# Setup the Turtle environment
speed(0)
bgcolor("black")
h = 0  # Initial hue for the HSV color model

# Drawing the pattern
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB
        color(c)  # Set the color
        h += 0.005  # Increment the hue for a smooth gradient
        right(90)  # Rotate right
        circle(150 - j * 6, 90)  # Draw a partial circle
        left(90)  # Rotate left
        circle(150 - j * 6, 90)  # Draw another partial circle
        right(180)  # Rotate back
    circle(40, 24)  # Rotate the whole structure

# Keep the window open
done()
