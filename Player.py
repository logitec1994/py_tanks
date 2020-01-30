class Player:
    name = ""
    score = 0

    def set_name(self, name):
        self.name = name

    def set_score(self, score=3):
        self.score += score