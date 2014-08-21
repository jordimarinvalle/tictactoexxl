# -*- coding: utf-8 -*-

import pytest

from tictactoexxl.board import Board
from tictactoexxl.board import BoardPosition
from tictactoexxl.board import BoardPositionError


class TestTicTacToeXXLBoard(object):

    board = None

    DIM_X = 3
    DIM_Y = 3

    POSITION_X_OK = "a"
    POSITION_Y_OK = "1"

    POSITION_X_KO = "x"
    POSITION_Y_KO = "8"

    SLOT_VALUE_DUMMY = "."

    def setup_method(self, _):
        self.board = Board(dim_x=self.DIM_X, dim_y=self.DIM_Y)

    def test_board_dimensions(self):
        assert self.board.dim_x == self.DIM_X
        assert self.board.dim_y == self.DIM_Y

    def test_board_num_slots(self):
        board_slots = self.board.dim_x * self.board.dim_y
        assert self.board.get_num_slots() is board_slots

    def test_board_slot_set_and_get(self):
        board_position = BoardPosition(self.POSITION_X_OK, self.POSITION_Y_OK)
        self.board.set_slot_value(board_position, self.SLOT_VALUE_DUMMY)
        slot_value = self.board.get_slot_value(board_position)
        assert slot_value is self.SLOT_VALUE_DUMMY

    def test_board_slot_do_exists(self):
        board_position = BoardPosition(self.POSITION_X_OK, self.POSITION_Y_OK)
        assert self.board.does_slot_exist(board_position) is True

    def test_board_slot_do_not_exists(self):
        board_position = BoardPosition(self.POSITION_X_KO, self.POSITION_Y_KO)
        assert self.board.does_slot_exist(board_position) is False

    def test_board_slot_is_available(self):
        board_position = BoardPosition(self.POSITION_X_OK, self.POSITION_Y_OK)
        assert self.board.is_slot_available(board_position) is True

    def test_board_slot_is_not_available(self):
        board_position = BoardPosition(self.POSITION_X_OK, self.POSITION_Y_OK)
        self.board.set_slot_value(board_position, self.SLOT_VALUE_DUMMY)
        assert self.board.is_slot_available(board_position) is False


class TestTicTacToeXXLBoardPosition(object):

    board_position = None

    POSITION_CORNER_UP_LEFT_X = "a"
    POSITION_CORNER_UP_LEFT_Y = "1"

    POSITION_NOT_IN_EDGE_X = "b"
    POSITION_NOT_IN_EDGE_Y = "2"

    def setup_method(self, _):
        self.board_position = BoardPosition(x=self.POSITION_NOT_IN_EDGE_X,
                                            y=self.POSITION_NOT_IN_EDGE_Y)

    def test_board_position_invalid(self):
        board_position = BoardPosition(x=self.POSITION_CORNER_UP_LEFT_X,
                                       y=self.POSITION_CORNER_UP_LEFT_Y)
        new_board_position = None
        try:
            new_board_position = board_position.get_position_up()
        except BoardPositionError:
            assert new_board_position is None

    def test_board_position_up(self):
        new_board_position = self.board_position.get_position_up()
        assert new_board_position.x == "a" and new_board_position.y == "2"

    def test_board_position_down(self):
        new_board_position = self.board_position.get_position_down()
        assert new_board_position.x == "c" and new_board_position.y == "2"

    def test_board_position_left(self):
        new_board_position = self.board_position.get_position_left()
        assert new_board_position.x == "b" and new_board_position.y == "1"

    def test_board_position_right(self):
        new_board_position = self.board_position.get_position_right()
        assert new_board_position.x == "b" and new_board_position.y == "3"

    def test_board_position_up_left(self):
        new_board_position = self.board_position.get_position_up_left()
        assert new_board_position.x == "a" and new_board_position.y == "1"

    def test_board_position_up_right(self):
        new_board_position = self.board_position.get_position_up_right()
        assert new_board_position.x == "a" and new_board_position.y == "3"

    def test_board_position_down_left(self):
        new_board_position = self.board_position.get_position_down_left()
        assert new_board_position.x == "c" and new_board_position.y == "1"

    def test_board_position_down_right(self):
        new_board_position = self.board_position.get_position_down_right()
        assert new_board_position.x == "c" and new_board_position.y == "3"


if __name__ == '__main__':
    pytest.main()
