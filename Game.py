
from Display import Display
from Logic import Logic

logic = Logic()

class Game:
    def run(self):
        logic.is_game = True
        print("Game is running")


    def stop(self):
        logic.is_game = False
        print("Game is stopped")