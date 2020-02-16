import canvas

class Game:
    def start_game(self):
        self.__canv = canvas.Canvas()
        self.__canv.create_canvas()
        self.__canv.set_zone()
        self.__canv.render()

    def add_element(self):
        self.__canv.create_canvas()