
class Canvas:
    """docstring for Canvas"""

    def __init__(self):
        self.size = {   
                        "width":    10,
                        "height":   10
                    }
        self.matrix = list()


    # Dimension manipulations
    def get_width(self):
        return self.size['width']

    def get_height(self):
        return self.size['height']

    def set_size(self, width:int, height:int):
        self.size['width'] = width
        self.size['height'] = height

    def set_width(self, width):
        self.size['width'] = width

    def set_height(self, height):
        self.size['height'] = height

    # Canvas face
    def new_buffer(self):
        self.matrix = [["|" for x in range(self.size["width"])] for y in range(self.size["height"])]

    def get_matrix(self):
        return self.matrix

    # def set_buff(self, char, x, y):
    #     self.matrix[x][y] = char

    def render(self):
        for row in self.matrix:
            print("".join( [str(line) for line in row] ) )
