# -*- coding: utf-8 -*-

import pytest

from tictactoexxl.player import Player


class TestTicTacToeXXLPlayer(object):

    player = None

    NAME = "tictactoexxl"
    MOVE_REPRESENTATION = "X"

    def setup_method(self, _):
        self.player = Player(self.NAME, self.MOVE_REPRESENTATION)

    def test_player_name(self):
        assert self.player.name is self.NAME

    def test_player_move_representation(self):
        assert self.player.move_repr is self.MOVE_REPRESENTATION


if __name__ == '__main__':
    pytest.main()
