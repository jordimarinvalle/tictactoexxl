# -*- coding: utf-8 -*-

import pytest

from tictactoexxl.grid import Grid
from tictactoexxl.grid import GridPosition


class TestTicTacToeXXLGrid(object):

    grid = None

    DIM_X = 3
    DIM_Y = 3

    def setup_method(self, _):
        self.grid = Grid(dim_x=self.DIM_X, dim_y=self.DIM_Y)

    def test_grid_dimensions(self):
        assert self.grid.dim_x == self.DIM_X
        assert self.grid.dim_y == self.DIM_Y

    def test_grid_create_grid(self):
        grid = Grid.create_grid(self.DIM_X, self.DIM_Y)
        slots = []
        for x, y_list_and_values in grid.items():
            for y, value in y_list_and_values.items():
                slots.append(y)
        assert len(slots) is (self.DIM_X * self.DIM_Y)


class TestTicTacToeXXLGridPosition(object):

    POSITION_X_0 = 0
    POSITION_Y_0 = 0

    POSITION_X_KO = -1
    POSITION_Y_KO = -1

    def setup_method(self, _):
        pass

    def test_grid_transform_board_coordinate_x(self):
        assert GridPosition.transform_board_coordinate_x("a") is 0

    def test_grid_transform_board_coordinate_y(self):
        assert GridPosition.transform_board_coordinate_y("1") is 0

    def test_grid_coordinates(self):
        grid_position = GridPosition(self.POSITION_X_0, self.POSITION_Y_0)
        assert grid_position.get_coordinates() == (self.POSITION_X_0,
                                                   self.POSITION_Y_0)

    def test_all_coordinates_x(self):
        expected_all_coordinates = [0, 1, 2, ]
        all_coordinates = GridPosition.get_x_all_coordinates(3)
        for coordinate_x in expected_all_coordinates:
            all_coordinates.remove(coordinate_x)
        assert len(all_coordinates) is 0

    def test_all_coordinates_y(self):
        expected_all_coordinates = [0, 1, 2, ]
        all_coordinates = GridPosition.get_y_all_coordinates(3)
        for coordinate_y in expected_all_coordinates:
            all_coordinates.remove(coordinate_y)
        assert len(all_coordinates) is 0

    def test_grid_position_valid(self):
        grid_position = GridPosition(self.POSITION_X_0, self.POSITION_Y_0)
        assert GridPosition.exists_position(grid_position) is True

    def test_grid_position_invalid(self):
        grid_position = GridPosition(self.POSITION_X_KO, self.POSITION_Y_KO)
        assert GridPosition.exists_position(grid_position) is False


if __name__ == '__main__':
    pytest.main()
