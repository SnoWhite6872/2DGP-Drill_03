from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def top_move():
    for x in range(20, 780, 10):
        boys_move(x, 50)
    pass


def right_move():
    pass


def bottom_move():
    pass


def left_move():
    pass


def rectangle_move():

    top_move()
    right_move()
    bottom_move()
    left_move()
    pass


def boys_move(x: float, y: float):
    clear_canvas()
    boy.draw_now(x, y)
    delay(0.1)


def triangle_move():
    pass


def circle_move():
    pass


while True:
    rectangle_move()
    triangle_move()
    circle_move()


    pass

    # break

close_canvas()