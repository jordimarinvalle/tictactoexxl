# -*- coding: utf-8 -*-

import os

from tictactoexxl.exception import TicTacToeXXLError


class Grid(object):
    '''
    The grid is designed to abstract the board positions (human & more readable
    board position) with the grid position (computing board positon).
    '''

    grid = None

    dim_x = None
    dim_y = None

    def __init__(self, dim_x, dim_y):
        '''
        Create a tic-tac-toe grid that has a None value for each grid position.

        Arguments:
        :dim_x -- integer, dimension of the grid (width)
        :dim_y -- integer, dimension of the grid (height)
        '''
        self.dim_x = dim_x
        self.dim_y = dim_y

        self.grid = Grid.create_grid(dim_x, dim_y)

    def __str__(self):
        '''
        Return a string representation of the grid.

        Returns: string
        '''
        strgrid = ""
        for x, y_list_and_values in self.grid.items():
            row = []
            for y, value in y_list_and_values.items():
                row.append("%s,%s: %s" % (x, y, value, ))
            strgrid = "%s%s%s" % (strgrid, " | ".join(row), os.linesep)
        return strgrid

    @staticmethod
    def create_grid(dim_x, dim_y):
        '''
        Create a grid.

        Arguments:
        :dim_x -- integer, dimension of the grid (width)
        :dim_y -- integer, dimension of the grid (height)

        Returns: dictionary
        '''
        grid_x_values = GridPosition.get_x_all_coordinates(dim_x)
        grid_y_values = GridPosition.get_y_all_coordinates(dim_y)

        grid = {}
        for x in grid_x_values:
            grid[x] = {}
            for y in grid_y_values:
                grid[x][y] = None
        return grid


class GridPosition(object):
    '''
    TicTacToe GridPosition has a coordinate x and a coordinate y.
    '''

    x = None
    y = None

    def __init__(self, x, y):
        '''
        Create a tic-tac-toe grid's position.
        '''
        self.x = x
        self.y = y

    def __str__(self):
        '''
        Return a string representation of the grid's position.

        Returns: string
        '''
        return "<%s,%s>" % (self.x, self.y, )

    def get_coordinates(self):
        '''
        Get x and y coordinates.

        Returns: tuple, two elements tuple
        '''
        return (self.x, self.y)

    @staticmethod
    def transform_board_coordinate_x(board_coordinate_x):
        '''
        Transform a board coordinate x to a grid coordinate x.

        Raises:
        :GridPositionError()

        Returns: integer
        '''
        try:
            return ord(str(board_coordinate_x)) - 97
        except TypeError:
            raise GridPositionError()

    @staticmethod
    def transform_board_coordinate_y(board_coordinate_y):
        '''
        Transform a board coordinate y to a grid coordinate y.

        Raises:
        :GridPositionError()

        Returns: integer
        '''
        try:
            return int(board_coordinate_y) - 1
        except (TypeError, ValueError):
            raise GridPositionError()

    @staticmethod
    def get_x_all_coordinates(grid_dim_x):
        '''
        Get all grid coordinates related with a grid dim x.

        Arguments:
        :grid_dim_x -- integer, dimension of the grid (width)

        Returns: list
        '''
        return [x for x in range(0, grid_dim_x)]

    @staticmethod
    def get_y_all_coordinates(grid_dim_y):
        '''
        Get all grid coordinates related with a grid dim y.

        Arguments:
        :grid_dim_y -- integer, dimension of the grid (height)

        Returns: list
        '''
        return [y for y in range(0, grid_dim_y)]

    @staticmethod
    def exists_coordinate_x(grid_coordinate_x):
        '''
        Return true if grid's coordinate x exists, otherwise false.

        Arguments:
        :grid_coordinate_x -- integer, grid's coordinate x

        Returns: boolean
        '''
        return True if grid_coordinate_x > -1 else False

    @staticmethod
    def exists_coordinate_y(grid_coordinate_y):
        '''
        Return true if grid's coordinate y exists, otherwise false.

        Arguments:
        :grid_coordinate_y -- integer, grid's coordinate y

        Returns: boolean
        '''
        return True if grid_coordinate_y > -1 else False

    @staticmethod
    def exists_position(grid_position):
        '''
        Return true if a grid position exists, otherwise false.

        Arguments:
        :grid_position -- GridPosition, a grid position

        Returns: boolean
        '''
        if GridPosition.exists_coordinate_x(grid_position.x):
            if GridPosition.exists_coordinate_x(grid_position.y):
                return True
        return False

class GridPositionError(TicTacToeXXLError):

    MESSAGE = "Invalid grid position"


class GridPositionInvalidExistenceError(GridPositionError):

    MESSAGE = "Invalid grid position, it does not exist"
