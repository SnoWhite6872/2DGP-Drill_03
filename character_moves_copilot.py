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
    # 정삼각형 중심 (cx, cy), 변의 길이 l
    cx, cy = 400, 300
    l = 400
    # 꼭짓점 좌표 계산
    points = []
    for i in range(3):
        angle_deg = 90 + i * 120
        angle_rad = math.radians(angle_deg)
        x = cx + l * math.cos(angle_rad) / 2
        y = cy + l * math.sin(angle_rad) / 2
        points.append((x, y))
    # 각 변을 따라 이동
    steps = 40
    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 3]
        for t in range(steps):
            x = x1 + (x2 - x1) * t / steps
            y = y1 + (y2 - y1) * t / steps
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
