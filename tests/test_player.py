from player import Player
from hole import Hole

class TestPlayer:
    def _get_player(self):
        return Player("Soléna")

    def test_get_score_returns_zero(self):
        player = self._get_player()
        assert player.get_score() == 0

    def test_set_score_sets_correctly(self):
        player = self._get_player()
        player.set_score(5)
        assert player.get_score() == 5

        player.set_score(10)
        assert player.get_score() == 10

        player.set_score(0)
        assert player.get_score() == 0

    def test_increment_score_increments_correctly(self):
        player = self._get_player()
        player.set_score(5)

        player.increment_score(4)
        assert player.get_score() == 9

        player.increment_score(2)
        assert player.get_score() == 11

        player.increment_score(18)
        assert player.get_score() == 29


