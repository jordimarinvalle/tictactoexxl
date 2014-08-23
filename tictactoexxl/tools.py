# -*- coding: utf-8 -*-

import os
import sys
import argparse

from tictactoexxl import GAME_N_IN_A_ROW_DEFAULT
from tictactoexxl import GAME_NUM_PLAYERS_DEFAULT

from tictactoexxl import BOARD_DIM_X_DEFAULT
from tictactoexxl import BOARD_DIM_Y_DEFAULT


class Argument(object):

    @staticmethod
    def get_input_args():
        arg_parser = argparse.ArgumentParser(
            description="Description of TicTacToeXXL")

        arg_parser.add_argument(
            '-w', '--win', type=int, required=False,
            default=GAME_N_IN_A_ROW_DEFAULT,
            help="number of consecutive player's squares to win the game")

        arg_parser.add_argument(
            '-x', '--dimx', type=int, required=False,
            default=BOARD_DIM_X_DEFAULT,
            help="board dimension x (number of horitzontal squares)")

        arg_parser.add_argument(
            '-y', '--dimy', type=int, required=False,
            default=BOARD_DIM_Y_DEFAULT,
            help="board dimension y (number of vertical squares)")

        arg_parser.add_argument(
            '-p', '--players', type=int, required=False,
            default=GAME_NUM_PLAYERS_DEFAULT,
            help="number of players")

        return vars(arg_parser.parse_args())


class Typewitter(object):

    INFO = "ii"
    ERROR = "ee"
    QUESTION = "qq"

    @staticmethod
    def message(message, log_type=None):
        if log_type is None:
            log_type = Typewitter.INFO
        return "[%s] %s" % (log_type, message)

    @staticmethod
    def log(message, log_type=None):
        print(Typewitter.message(message, log_type))

    @staticmethod
    def input(message, log_type=None):
        return Py2Py3.input(Typewitter.message(message, log_type))

    @staticmethod
    def exit(message):
        sys.exit(Typewitter.message(message, Typewitter.ERROR))


class Message(object):

    @staticmethod
    def welcome():
        return "WELCOME TO TIC-TAC-TOE XXL (a simple tic-tac-toe game " \
            "with XXL fun)"

    @staticmethod
    def provide_player_name(player_name_auto):
        return "Please, %s, provide your name / alias " \
            "(default: %s): " % (player_name_auto, player_name_auto)

    @staticmethod
    def provide_player_move_representation(player_name, player_move_repr_auto):
        return "Please, player *%s*, provide a representative action " \
            "character (default %s): " % (player_name, player_move_repr_auto)

    @staticmethod
    def player_make_move(player_name):
        return "Player *%s*, please, make a move. " % (player_name)

    @staticmethod
    def provide_player_make_move_x():
        return "Provide coordinate x: "

    @staticmethod
    def provide_player_make_move_y():
        return "Provide coordinate y: "

    @staticmethod
    def game_won(player_name):
        return "PLAYER %s WON." % (player_name)

    @staticmethod
    def game_tie():
        return "NO ONE WON. TIE."


class Screen(object):

    @staticmethod
    def clear():
        '''
        Clear the screen in the command shell.

        Notes:
        - It works on Windows and Unix based systems
        '''
        os.system(['clear', 'cls'][os.name == 'nt'])


class Py2Py3(object):
    '''
    A helper class that provides a bit more compatibility between python2.x
    and python3.x without python package 'future' need.
    '''

    @staticmethod
    def input(prompt):
        if sys.version_info[:2][0] > 2:
            return input(prompt)
        else:
            return raw_input(prompt)
