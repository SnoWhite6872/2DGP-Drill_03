from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def top_move():
    pass


def right_move():
    pass


def bottom_move():
    pass


def left_move():
    pass


def rectangle_move():
    clear_canvas()
    top_move()
    right_move()
    bottom_move()
    left_move()

    boy.draw_now(400, 300)
    delay(0.1)
    pass


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