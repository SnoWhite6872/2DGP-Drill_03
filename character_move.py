from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def bottom_move():
    for x in range(20, 780, 10):
        boys_move(x, 50)
    pass


def right_move():
    for y in range(50,550,10):
        boys_move(780, y)
    pass


def top_move():
    for x in range(780,20,-10):
        boys_move(x, 550)
    pass


def left_move():
    for y in range(550,50,-10):
        boys_move(20, y)
    pass


def rectangle_move():

    bottom_move()
    right_move()
    top_move()
    left_move()
    pass


def boys_move(x: float, y: float):
    clear_canvas()
    boy.draw_now(x, y)
    delay(0.1)


def upslash_move():
    x = 780
    y = 50
    while (x >400 and y<430):
        boys_move(x, y)
        x -= 10
        y += 10

    pass

def downslash_move():
    x = 400
    y = 430
    while (x > 20 and y > 50):
        boys_move(x, y)
        x -= 10
        y -= 10
    pass


def triangle_move():
    bottom_move()
    upslash_move()
    downslash_move()
    pass


def circle_move():
    r = 250
    for deg in range(0, 360, 10):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        boys_move(x, y)
    pass


while True:
    rectangle_move()
    triangle_move()
    circle_move()


    pass

    # break

close_canvas()