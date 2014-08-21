# -*- coding: utf-8 -*-

import pytest

from tictactoexxl.game import Game
from tictactoexxl.board import Board
from tictactoexxl.board import BoardPosition
from tictactoexxl.player import Player


class TestTicTacToeXXLGame(object):

    board = None
    player1 = None
    player2 = None

    PLAYER1_NAME = "ttt"
    PLAYER1_MOVE_REPRESENTATION = "M"

    PLAYER2_NAME = "tttxxl"
    PLAYER2_MOVE_REPRESENTATION = "W"

    def setup_method(self, _):

        self.board = Board()
        self.player1 = Player(self.PLAYER1_NAME,
                              self.PLAYER1_MOVE_REPRESENTATION)
        self.player2 = Player(self.PLAYER2_NAME,
                              self.PLAYER2_MOVE_REPRESENTATION)

        self.game = Game(board=self.board,
                         players=[self.player1, self.player2])

    def test_game_players(self):
        assert len(self.game.players) is 2

    def test_game_get_players_move_representations(self):
        set_1 = set(self.game.get_players_move_representations())
        set_2 = set([self.PLAYER1_MOVE_REPRESENTATION,
                    self.PLAYER2_MOVE_REPRESENTATION])
        assert set_2.difference(set_1) == set()

    def test_game_player_make_a_move(self):
        board_position = BoardPosition("a", "1")
        self.game.player_make_a_move(self.player1, board_position)
        slot_value = self.game.board.get_slot_value(board_position)
        assert slot_value is self.player1.move_repr

    def test_game_has_player_won(self):
        board_position_1 = BoardPosition("a", "1")
        self.game.player_make_a_move(self.player1, board_position_1)

        board_position_2 = BoardPosition("a", "2")
        self.game.player_make_a_move(self.player1, board_position_2)

        board_position_3 = BoardPosition("a", "3")
        self.game.player_make_a_move(self.player1, board_position_3)

        assert self.game.has_player_won(self.player1, board_position_3) is True


if __name__ == '__main__':
    pytest.main()
