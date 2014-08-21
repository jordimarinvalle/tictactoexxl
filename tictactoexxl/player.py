# -*- coding: utf-8 -*-

from tictactoexxl.exception import TicTacToeXXLError

from tictactoexxl import PLAYER_1_MOVE_REPR_DEFAULT, PLAYER_2_MOVE_REPR_DEFAULT


class Player(object):
    '''
    TicTacToe Player that mainly has a name and a move representation
    character.
    '''

    name = None
    move_repr = None

    def __init__(self, name, move_repr):
        '''
        Create a new tic-tac-toe player.

        Arguments:
        :name -- string, player's name
        :move_repr -- string, move representation character(s)
        '''
        self.name = name
        self.move_repr = move_repr

    def __str__(self):
        '''
        Get a custom string representation of the self player object.

        Returns: string
        '''
        return "<%s %s>" % (self.name, self.move_repr)

    @staticmethod
    def get_name_auto(player_id):
        '''
        Get a auto generated player's name with a sufix.
        i.e.: 2, will return, PLAYER_2

        Arguments:
        :player_id -- integer, a number

        Returns: string
        '''
        return "PLAYER_%s" % (player_id)

    @staticmethod
    def get_move_repr_auto(player_id):
        '''
        Get a auto generated player's movement representation.

        Arguments:
        :player_id -- integer, a number

        Returns: string
        '''
        try:
            return Player.get_standard_move_repr(player_id)
        except PlayerMoveRepresentationError:
            return "%s" % (player_id)

    @staticmethod
    def get_standard_move_repr(player_id):
        '''
        Get a standard player's movement representation based in player's id.

        Notes:
        - Based in two players tic-tac-toe basic game.

        Arguments:
        :player_id -- integer, a number

        Raises:
        :PlayerMoveRepresentationError()

        Returns: string
        '''
        standard_move_reprs = {
            1: PLAYER_1_MOVE_REPR_DEFAULT,
            2: PLAYER_2_MOVE_REPR_DEFAULT,
        }
        try:
            return standard_move_reprs[player_id]
        except KeyError:
            raise PlayerMoveRepresentationError()

    def has_board_slot_mark_as_player(self, board, board_position):
        '''
        Returns true if the position has been mark as a player's board positon,
        for a board, otherwise false.

        Arguments:
        :board -- Board, the game's board
        :board_position -- BoardPosition, a board position

        Returns: boolean
        '''
        if self.move_repr is board.get_slot_value(board_position):
            return True
        return False


class PlayerError(TicTacToeXXLError):

    MESSAGE = "Invalid player"


class PlayerMoveRepresentationError(PlayerError):

    MESSAGE = "Invalid player, move repr is not valid"
