from defines import *


class Canvas:
    def create_canvas(self):
        self.canvas = ([[" " for x in range(SIZE["width"])] for y in range(SIZE["height"])])
        return self.canvas

    def render(self):
        for row in self.canvas:
            print("".join([str(line) for line in row]))

    def get_canvas(self):
        return self.canvas

    def set_zone(self):  # may return SIZE
        for x in range(SIZE["height"]):
            for y in range(SIZE["width"]-2):
                if y == 0 or y == SIZE["width"]-3:
                    self.canvas[x][y] = "|"
                elif x == 0 or x == SIZE["height"]-1:
                    self.canvas[x][y] = "-"