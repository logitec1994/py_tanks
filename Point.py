
class Point:

    def __init__(self):
        self.__x = 0
        self.__y = 0


    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, x:int):
        self.__x = x
    def set_y(self, y:int):
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
