class Tank:
    health = 10
    position =  {
                    "x": 0,
                    "y": 0
                }

    def setX(self, x):
        self.position["x"] = x

    def setY(self, y):
        self.position["y"] = y

    def move_to(self, side, val=1):
        if side == "L":
            self.position["x"] -= val
        elif side == "R":
            self.position["x"] += val
        elif side == "U":
            self.position["y"] -= val
        elif side == "D":
            self.position["y"] += val
        else:
            print("Incorrect side")