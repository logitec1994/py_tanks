from defines import *
import os


class Canvas:
    def create_canvas(self):
        self.canvas = ([[" " for x in range(SIZE["width"])] for y in range(SIZE["height"])])

    def render(self):
        os.system("cls")
        for row in self.canvas:
            print("".join([str(line) for line in row]))

    def add_elem(self, elem):
        # self.canvas[elem["y"]][elem["x"]] = elem["face"]
        self.elem = elem
        return self.elem

    def update(self, posX, posY, face):
        self.canvas[posY][posX] = face

    def get_canvas(self):
        return self.canvas

    def set_zone(self):  # may return SIZE
        for x in range(SIZE["height"]):
            for y in range(SIZE["width"]-2):
                if y == 0 or y == SIZE["width"]-3:
                    self.canvas[x][y] = "|"
                elif x == 0 or x == SIZE["height"]-1:
                    self.canvas[x][y] = "-"