import abc
from os import system

class IMovable(abc.ABC):

    @abc.abstractmethod
    def move_to(self, side):
        pass


class Tank(IMovable):
    def move_to(self, side):
        pass

    def shoot(self):
        pass


class Field:
    def __init__(self, h, w):
        self.height = h
        self.width = w

class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    def get_position(self):
        pos = [self.__x, self.__y]
        return pos

class Player(Point):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.__is_alive = True

    def kill(self):
        self.__is_alive = False
        return self.__is_alive

class Battle:
    __is_active = False

    def __init__(self):
        self.__players = list()

    def switch_state(self):
        if self.__is_active == False:
            self.__is_active = True
        else:
            self.__is_active = False

    def get_state(self):
        return self.__is_active

    def add_player(self, player: Player):
        self.__players.append(player)
        return self.__players


    def __str__(self):
        ps = ""
        for player in self.__players:
            ps += f"[Player name: {player.name}]\n[Player health: {player.health}]\n\n"
        return f"Battle status is: {self.__is_active}\n{ps}"


class Canvas:
    def __init__(self, h, w):
        self.heigh = h
        self.width = w

    def fill(self):
        self.content = [ ["1" for x in range(self.width)] for y in range(self.heigh) ]
        return self.content

    def fill_on(self, x, y):
        self.content[x][y] = "@"

    def add_walls(self):
        for line in range(self.heigh):
            for rows in range(self.width):
                if line == 0 or line == self.heigh-1:
                    self.content[line][rows] = "#"
                elif rows == 0 or rows == self.width-1:
                    self.content[line][rows] = "#"

    def draw(self):
        system("clear")
        for row in self.content:
            print("".join([str(line) for line in row]))


# t = Tank()
# b = Battle(t)

# c = Canvas(10, 30)
# c.fill()
# # print(c.content)
# # print(len(c.content))

# # c.fill_on(2, 3)
# c.add_walls()
# c.draw()


class Game:
    def __init__(self):
        pass

    def play(self):
        battle = Battle()
        canvas = Canvas(10, 50)
        name = input("Enter your name: ")
        player = Player(name)
        print(f"\n{name}, prepare to FIGHT!")
        battle.add_player(player)
        battle.switch_state()
        canvas.fill()
        # костыльное решение создать экземпляр класса с помощью метода move_to
        player.move_to(25, 5)
        canvas.fill_on(player.get_position()[1], player.get_position()[0])
        while battle.get_state():
            canvas.draw()
            # print(player1.get_position()[0])
            # print(player1.get_position()[1])
            print(battle)
            battle.switch_state()


g = Game()
g.play()
