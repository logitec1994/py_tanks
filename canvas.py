class Canvas:
    def __init__(self, size):
        self.size = size

    def create_canvas(self):
        canvas: list
        canvas = ([[" " for x in range(self.size["width"])] for y in range(self.size["height"])])
        return canvas
