
class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.score: int = 0

    def __str__(self) -> str:
        return f"name: {self.name}, score: {self.score}"


    def get_score(self) -> int:
        return self.score


    def increment_score(self, nb: int):
        self.score += nb


