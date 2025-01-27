
class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0


    def get_score(self)-> int:
        return self.score

    def set_score(self, nb: int):
        self.score = nb

    def increment_score(self, nb: int):
        self.score += nb


