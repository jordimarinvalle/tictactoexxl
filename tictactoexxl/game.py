# -*- coding: utf-8 -*-

import os
import copy

from tictactoexxl.board import Board
from tictactoexxl.board import BoardPosition
from tictactoexxl.board import BoardPositionError
from tictactoexxl.board import GridPosition
from tictactoexxl.player import Player
from tictactoexxl.exception import TicTacToeXXLError

from tictactoexxl import GAME_N_IN_A_ROW_DEFAULT
from tictactoexxl import BOARD_DIM_X_DEFAULT, BOARD_DIM_Y_DEFAULT
from tictactoexxl import PLAYER_1_NAME_DEFAULT, PLAYER_1_MOVE_REPR_DEFAULT
from tictactoexxl import PLAYER_2_NAME_DEFAULT, PLAYER_2_MOVE_REPR_DEFAULT


class Game(object):
    '''
    TicTacToe Game class that mainly has a board and a list of players.
    '''

    winner = None

    players = []

    board = None
    n_in_a_row = None

    NUM_PLAYERS_TO_PLAY_MIN = 2

    def __init__(self, board=None, n_in_a_row=None, players=[]):
        '''
        Initializes a game for the parameters given. Basic parameters are not
        pass to Game constructor game will be as a usual tic-tac-toe game
        (no XXL fun).

        Arguments:
        :board -- Board (default None), a board instance
        :n_in_a_row -- integer (default None), number of how many consecutive
                       player's movements are required to win a game
        :players -- list (default []), a list of Player instances

        Raises:
        :GameSetupWinningError()
        '''

        if board is None:
            board = Board(BOARD_DIM_X_DEFAULT, BOARD_DIM_Y_DEFAULT)

        if n_in_a_row is None:
            n_in_a_row = GAME_N_IN_A_ROW_DEFAULT

        if players is None or len(players) < Game.NUM_PLAYERS_TO_PLAY_MIN:
            players = [
                Player(PLAYER_1_NAME_DEFAULT, PLAYER_1_MOVE_REPR_DEFAULT),
                Player(PLAYER_2_NAME_DEFAULT, PLAYER_2_MOVE_REPR_DEFAULT),
            ]

        self.board = board
        self.n_in_a_row = int(n_in_a_row)
        self.players = players

        if Game.is_winning_n_in_a_row_ok(num_players=len(players),
                                         board_dim_x=board.dim_x,
                                         board_dim_y=board.dim_y,
                                         n_in_a_row=n_in_a_row) is False:
            raise GameSetupWinningError()

    def __str__(self):
        '''
        Return a string representation of the game.

        Returns: string
        '''
        strgrid = ""
        for x, y_values in self.board.grid.items():
            row = []
            for y, grid_bucket_value in y_values.items():
                board_position = BoardPosition.transform_grid_position(
                    GridPosition(x, y))
                slot_value = self.board.get_slot_value(board_position)
                row.append("%s,%s: %s" % (board_position.x,
                                          board_position.y,
                                          slot_value))
            strgrid = "%s%s%s" % (strgrid, " | ".join(row), os.linesep)
        return strgrid

    @staticmethod
    def is_winning_n_in_a_row_ok(
            num_players, board_dim_x, board_dim_y, n_in_a_row):
        '''
        Return true if game setup params are ok for a fair game.

        Arguments:
        :num_players -- integer, number of players
        :board_dim_x -- integer, board x length
        :board_dim_y -- integer, board y length
        :n_in_a_row -- integer, number of how many players movements are
                       required to win a game

        Returns: boolean
        '''
        if board_dim_x * board_dim_y > (num_players * n_in_a_row) - 1:
            return True
        return False

    def get_player(self, i_round):
        '''
        Get a player for the round of the tictactoe game.
        e.g.: there is a game with three players, is the fourth round,
        then first player will be returned.

        Arguments:
        :i_round -- integer, the round number of the game

        Returns: Player
        '''
        return self.players[i_round % len(self.players)]

    def get_players_move_representations(self):
        '''
        Get all players move representations.

        Returns: list
        '''
        move_reprs = []
        for player in self.players:
            move_reprs.append(player.move_repr)
        return move_reprs

    def player_make_a_move(self, player, board_position):
        '''
        Alter game board with a player's board prosition.

        Arguments:
        :player -- Player, a player's game
        :board_position -- BoardPosition, a board's position

        Returns: Board
        '''
        self.board.add_player_move(board_position, player.move_repr)
        return self.board

    def has_player_won(self, player, last_board_position=None):
        '''
        Returns true if the last board position movement of a game's player
        made him won the game otherwise false.

        Arguments:
        :player -- Player, a player's game
        :last_board_position -- BoardPosition, a board's position

        Returns: boolean
        '''

        if last_board_position is None:
            raise GameLastBoardPositionError()

        if player.has_board_slot_mark_as_player(
                self.board, last_board_position) is False:
            raise GameLastBoardPositionInvalidError()

        for direction in self.board.get_directions():

            a_board_position = copy.deepcopy(last_board_position)
            on_the_way_to_win = [str(a_board_position), ]

            for i in range(0, self.n_in_a_row - 1):
                try:
                    a_board_position = last_board_position.get_next(
                        a_board_position, direction)
                    if player.has_board_slot_mark_as_player(self.board,
                                                            a_board_position):
                        on_the_way_to_win.append(str(a_board_position))
                        if len(on_the_way_to_win) is self.n_in_a_row:
                            return True
                    else:
                        direction = self.board.get_complementary_direction(
                            direction)

                except BoardPositionError:
                    break

        return False


class GameError(TicTacToeXXLError):

    MESSAGE = "Game error"


class GameSetupWinningError(GameError):

    MESSAGE = "Game error, setup params will not create a fair game."


class GameLastBoardPositionError(GameError):

    MESSAGE = "Game error, last board position"


class GameLastBoardPositionInvalidError(GameError):

    MESSAGE = "Game error, last board position does not belong to the player"
