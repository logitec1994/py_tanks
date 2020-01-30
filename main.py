import os

from defines import *
import canvas

# def render(field: list):
#     for row in field:
#         print("".join([str(line) for line in row]))

field = canvas.Canvas()
os.system("cls")  # on Windows
field.create_canvas()
field.set_zone()
field.render()

