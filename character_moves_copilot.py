from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def boys_move(x: float, y: float):
    clear_canvas()
    boy.draw_now(x, y)
    delay(0.1)

def bottom_move():
    for x in range(20, 780, 10):
        boys_move(x, 50)

def right_move():
    for y in range(50, 550, 10):
        boys_move(780, y)

def top_move():
    for x in range(780, 20, -10):
        boys_move(x, 550)

def left_move():
    for y in range(550, 50, -10):
        boys_move(20, y)

def rectangle_move():
    bottom_move()
    right_move()
    top_move()
    left_move()

def triangle_move():
    # bottom
    for x in range(20, 780, 10):
        boys_move(x, 50)
    # upslash
    for i in range(0, 38):
        x = 780 - i * 10
        y = 50 + i * 10
        boys_move(x, y)
    # downslash
    for i in range(0, 38):
        x = 400 - i * 10
        y = 430 - i * 10
        boys_move(x, y)

def circle_move():
    r = 250
    for deg in range(0, 360, 10):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        boys_move(x, y)

while True:
    rectangle_move()
    triangle_move()
    circle_move()

close_canvas()

