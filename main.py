import os

from defines import *
import canvas


def add_walls(field: list):
    for x in range(SIZE["height"]):
        for y in range(SIZE["width"]-2):
            if y == 0 or y == SIZE["width"]-3:
                field[x][y] = "|"
            elif x == 0 or x == SIZE["height"]-1:
                field[x][y] = "-"


def render(field: list):
    for row in field:
        print("".join([str(line) for line in row]))


field = canvas.Canvas(SIZE).create_canvas()
add_walls(field)
os.system("cls")
render(field)
