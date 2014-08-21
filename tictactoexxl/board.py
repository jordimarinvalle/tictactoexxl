# -*- coding: utf-8 -*-

import os

from tictactoexxl.grid import Grid
from tictactoexxl.grid import GridPosition
from tictactoexxl.grid import GridPositionError
from tictactoexxl.exception import TicTacToeXXLError

from tictactoexxl import BOARD_DIM_X_DEFAULT, BOARD_DIM_Y_DEFAULT


class Board(object):
    '''
    TicTacToe Board that has a fixed x and y dimensions, and with them
    it generate a grid.
    '''

    grid = None

    dim_x = None
    dim_y = None

    SLOT_EMPTY = " "

    DIRECTION_UP = "up"
    DIRECTION_DOWN = "down"
    DIRECTION_LEFT = "left"
    DIRECTION_RIGHT = "right"
    DIRECTION_UP_LEFT = "up_left"
    DIRECTION_UP_RIGHT = "up_right"
    DIRECTION_DOWN_LEFT = "down_left"
    DIRECTION_DOWN_RIGHT = "down_right"

    def __init__(self, dim_x=None, dim_y=None):
        '''
        Create a new tic-tac-toe board with a Grid abstraction to deal with
        the coordinates provided by the players.

        Arguments:
        :dim_x -- integer (default None), dimension of the board (width)
        :dim_y -- integer (default None), dimension of the board (height)

        Notes:
        :slot -- a slot is where a cordinate x gets with a cordinate y,
                 AKA board position bucket.
        :direction -- string, a board's direction row direction:
                      vertical, horitzontal and diagonal.

        '''
        if dim_x is None:
            dim_x = BOARD_DIM_X_DEFAULT

        if dim_y is None:
            dim_y = BOARD_DIM_Y_DEFAULT

        self.dim_x = dim_x
        self.dim_y = dim_y

        self.grid = Grid(dim_x, dim_y).grid

    def __str__(self):
        '''
        Return a string representation of the board.

        Returns: string
        '''
        strgrid = ""
        for x, y_values in self.grid.items():
            row = []
            for y, grid_bucket_value in y_values.items():
                board_position = BoardPosition.transform_grid_position(
                    GridPosition(x, y))
                row.append("%s,%s" % (board_position.x, board_position.y, ))
            strgrid = "%s%s%s" % (strgrid, " | ".join(row), os.linesep)
        return strgrid

    def get_slots(self):
        '''
        Get a list of board's slots.

        Returns: list
        '''
        slots = []
        for x, y_list_and_values in self.grid.items():
            for y, value in y_list_and_values.items():
                slots.append(value)
        return slots

    def get_num_slots(self):
        '''
        Get how many slots has the board.

        Returns: integer
        '''
        return len(self.get_slots())

    def get_slot_value(self, board_position):
        '''
        Get the board position value for a BoardPosition provided.
        In case that slot has a <None> value, a Board.SLOT_EMPTY
        will be returned.

        Arguments:
        :board_position -- BoardPosition, a board's position

        Returns: string
        '''
        if self.does_slot_exist(board_position) is False:
            raise BoardPositionInvalidExistenceError()

        slot_value = self.grid[board_position.grid.x][board_position.grid.y]

        if slot_value is None:
            return Board.SLOT_EMPTY
        return slot_value

    def set_slot_value(self, board_position, value):
        '''
        Set a value for a BoardPosition provided.

        Arguments:
        :board_position -- BoardPosition, a board's position
        :value -- string, a simple string that represents a player's movement

        Raises:
        :BoardPositionInvalidExistenceError()
        :BoardPositionInvalidAvailabilityError()

        Notes:
        - The board position must exists in the board and
          has to be available to add a player move.
        '''
        if self.does_slot_exist(board_position) is False:
            raise BoardPositionInvalidExistenceError()
        if self.is_slot_available(board_position) is False:
            raise BoardPositionInvalidAvailabilityError()

        self.grid[board_position.grid.x][board_position.grid.y] = value

    def does_slot_exist(self, board_position):
        '''
        Returns true if a slot (AKA board position bucket) exists,
        otherwise false.

        Arguments:
        :board_position -- BoardPosition, a board's position

        Returns: boolean
        '''
        try:
            self.grid[board_position.grid.x][board_position.grid.y]
            return True
        except KeyError:
            return False

    def is_slot_available(self, board_position):
        '''
        Returns true if a slot (AKA board position bucket) is available,
        otherwise false.

        Arguments:
        :board_position -- BoardPosition, a board's position

        Returns: boolean
        '''
        if self.get_slot_value(board_position) is Board.SLOT_EMPTY:
            return True
        return False

    def add_player_move(self, board_position, player_move_repr):
        '''
        Add a player move into the board. Board's slot can not be unmark,
        once is mark by a player's movement representation.

        Arguments:
        :board_position -- BoardPosition, a board's position
        :player_move_repr -- string, a player's movement representation
        '''
        self.set_slot_value(board_position, player_move_repr)

    def get_directions(self):
        '''
        Get a list of all the board's directions that might be userd to
        determine a winner.

        Returns: list

        Notes:
        :direction -- string, a board's direction row direction:
                      vertical, horitzontal and diagonal.
        '''
        return [
            Board.DIRECTION_UP, Board.DIRECTION_DOWN,
            Board.DIRECTION_LEFT, Board.DIRECTION_RIGHT,
            Board.DIRECTION_UP_LEFT, Board.DIRECTION_UP_RIGHT,
            Board.DIRECTION_DOWN_LEFT, Board.DIRECTION_DOWN_RIGHT,
        ]

    def get_complementary_direction(self, direction):
        '''
        Get a complementary direction that might be used to determine a winner.

        Arguments:
        direction -- string, a board's winning direction

        Returns: string

        Notes:
        :direction -- string, a board's direction row direction:
                      vertical, horitzontal and diagonal.
        '''
        complementary_directions = {
            Board.DIRECTION_UP: Board.DIRECTION_DOWN,
            Board.DIRECTION_DOWN: Board.DIRECTION_UP,
            Board.DIRECTION_LEFT: Board.DIRECTION_RIGHT,
            Board.DIRECTION_RIGHT: Board.DIRECTION_LEFT,
            Board.DIRECTION_UP_LEFT: Board.DIRECTION_DOWN_RIGHT,
            Board.DIRECTION_UP_RIGHT: Board.DIRECTION_DOWN_LEFT,
            Board.DIRECTION_DOWN_LEFT: Board.DIRECTION_DOWN_RIGHT,
            Board.DIRECTION_DOWN_RIGHT: Board.DIRECTION_DOWN_LEFT,
        }
        return complementary_directions[direction]


class BoardPosition(object):
    '''
    TicTacToe BoardPosition has a coordinate x and a coordinate y, also has a
    equivalent of a GridPosition (which is a 'no-human' readable coordinate
    x and coordinate y).
    '''

    x = None
    y = None

    grid_position = None

    grid_x = None
    grid_y = None

    def __init__(self, x, y):
        '''
        Create a tic-tac-toe board's position.

        Arguments:
        :x -- string, coordinate x
        :y -- string, coordinate y

        Raises:
        :BoardPositionError()
        '''
        try:
            self.x = x
            self.y = y

            grid_coordinate_x = GridPosition.transform_board_coordinate_x(x)
            grid_coordinate_y = GridPosition.transform_board_coordinate_y(y)

            self.grid = GridPosition(grid_coordinate_x, grid_coordinate_y)

        except GridPositionError:
            raise BoardPositionError()

    def __str__(self):
        '''
        Return a string representation of the board's position.

        Returns: string
        '''
        return "<%s,%s>" % (self.x, self.y)

    def get_coordinates(self):
        '''
        Get x and y coordinates.

        Returns: tuple, two elements tuple
        '''
        return (self.x, self.y)

    @staticmethod
    def transform_grid_position_x(x):
        '''
        Transform a grid coordinate x to a board coordinate x.

        Returns: string
        '''
        return chr(int(x) + ord('a'))

    @staticmethod
    def transform_grid_position_y(y):
        '''
        Transform a grid coordinate x to a board coordinate x.

        Returns: string
        '''
        return str(int(y) + 1)

    @staticmethod
    def transform_grid_position(grid_position):
        '''
        Transform a grid's position into a board's position.

        Arguments:
        :grid_position -- GridPosition, a grid's position.

        Returns: BoardPosition
        '''
        x = BoardPosition.transform_grid_position_x(grid_position.x)
        y = BoardPosition.transform_grid_position_y(grid_position.y)
        return BoardPosition(x, y)

    @staticmethod
    def move_to_position(grid_position):
        '''
        By a grid's position, move by an 'abstract' cursor to a board's
        position.

        Arguments:
        :grid_position -- GridPosition, a grid's position.

        Raises:
        :BoardPositionError()

        Returns: BoardPosition
        '''
        if GridPosition.exists_position(grid_position):
            return BoardPosition.transform_grid_position(grid_position)
        raise BoardPositionError()

    def get_position_up(self):
        '''
        If exists, get the up position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x - 1,
                                     self.grid.y)
        return BoardPosition.move_to_position(grid_position)

    def get_position_down(self):
        '''
        If exists, get the down position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x + 1,
                                     self.grid.y)
        return BoardPosition.move_to_position(grid_position)

    def get_position_left(self):
        '''
        If exists, get the left position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x,
                                     self.grid.y - 1)
        return BoardPosition.move_to_position(grid_position)

    def get_position_right(self):
        '''
        If exists, get the right position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x,
                                     self.grid.y + 1)
        return BoardPosition.move_to_position(grid_position)

    def get_position_up_left(self):
        '''
        If exists, get the up left position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x - 1,
                                     self.grid.y - 1)
        return BoardPosition.move_to_position(grid_position)

    def get_position_up_right(self):
        '''
        If exists, get the up right position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x - 1,
                                     self.grid.y + 1)
        return BoardPosition.move_to_position(grid_position)

    def get_position_down_left(self):
        '''
        If exists, get the down left position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x + 1,
                                     self.grid.y - 1)
        return BoardPosition.move_to_position(grid_position)

    def get_position_down_right(self):
        '''
        If exists, get the down right position for the instanciated
        position's board.

        Returns: BoardPosition
        '''
        grid_position = GridPosition(self.grid.x + 1,
                                     self.grid.y + 1)
        return BoardPosition.move_to_position(grid_position)

    def get_positions(self):
        '''
        Get a dictionary with directions and self (BoardPosition)
        function names.

        Returns: dictionary
        '''
        return {
            Board.DIRECTION_UP: self.get_position_up,
            Board.DIRECTION_DOWN: self.get_position_down,
            Board.DIRECTION_LEFT: self.get_position_left,
            Board.DIRECTION_RIGHT: self.get_position_right,
            Board.DIRECTION_UP_LEFT: self.get_position_up_left,
            Board.DIRECTION_UP_RIGHT: self.get_position_up_right,
            Board.DIRECTION_DOWN_LEFT: self.get_position_down_left,
            Board.DIRECTION_DOWN_RIGHT: self.get_position_down_right,
        }

    def get_directions(self):
        '''
        Get all board direction's positions.

        Returns: list
        '''
        return self.get_positions().keys()

    def get_next(self, board_position, direction):
        '''
        Get the next board's position in function of a board's position and a
        direction.

        Arguments:
        :board_position -- BoardPosition, a board's position
        :direction -- string, a direction

        Returns: BoardPosition
        '''
        return board_position.get_positions()[direction]()


class BoardPositionError(TicTacToeXXLError):

    MESSAGE = "Invalid board position"


class BoardPositionInvalidExistenceError(BoardPositionError):

    MESSAGE = "Invalid board position, it does not exist"


class BoardPositionInvalidAvailabilityError(BoardPositionError):

    MESSAGE = "Invalid board position, it is not available"
