import canvas

class Tank(canvas.Canvas):
    def __init__(self):
        self.face = "@"
        self.postion = {
            "x": 4,
            "y": 4
        }

    def create_tank(self):
        return self.face

    def set_tank(self, face = "@"):
        self.face = face

    def move_left(self):
        self.postion["x"] -= 1
    def move_right(self):
        self.postion["x"] += 1
    def move_up(self):
        self.postion["y"] -= 1
    def move_down(self):
        self.postion["y"] += 1
