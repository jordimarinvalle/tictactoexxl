#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tictactoexxl.tools import Argument
from tictactoexxl.tools import Typewitter
from tictactoexxl.tools import Message
from tictactoexxl.tools import Screen

from tictactoexxl.game import Game
from tictactoexxl.game import GameError

from tictactoexxl.player import Player

from tictactoexxl.board import Board
from tictactoexxl.board import BoardError
from tictactoexxl.board import BoardPosition
from tictactoexxl.board import BoardPositionError


def play(dimx=None, dimy=None, win=None, players=[]):

    try:
        game = Game(Board(dimx, dimy), win, players)
    except (GameError, BoardError) as e:
        Typewitter.exit(str(e))

    for i in range(0, game.board.get_num_slots()):

        Screen.clear()

        if game.winner:
            break

        player = game.get_player(i)

        print(game)

        while 1:
            Typewitter.log(Message.player_make_move(player.name),
                           Typewitter.INFO)

            try:
                x = Typewitter.input(Message.provide_player_make_move_x(),
                                     Typewitter.QUESTION)
                y = Typewitter.input(Message.provide_player_make_move_y(),
                                     Typewitter.QUESTION)

                board_position = BoardPosition(x, y)
                game.player_make_a_move(player, board_position)
                break

            except (GameError, BoardPositionError) as e:
                Typewitter.log(str(e), Typewitter.ERROR)

        if game.has_player_won(player, board_position):
            game.winner = player

    Screen.clear()

    print(game)

    if game.winner:
        Typewitter.log(Message.game_won(player.name), Typewitter.INFO)

    if game.winner is None:
        Typewitter.log(Message.game_tie(), Typewitter.INFO)


if __name__ == "__main__":

    arguments = Argument.get_input_args()

    Screen.clear()
    Typewitter.input(Message.welcome(), Typewitter.INFO)

    players = []
    for p in range(0, arguments['players']):
        player_id = len(players) + 1
        player_name_auto = Player.get_name_auto(player_id)
        player_move_repr_auto = Player.get_move_repr_auto(player_id)

        message_player_name = Message.provide_player_name(player_name_auto)
        player_name = Typewitter.input(message_player_name,
                                       Typewitter.QUESTION)
        if not player_name:
            player_name = player_name_auto

        message_player_move_repr = Message.provide_player_move_representation(
            player_name, player_move_repr_auto)
        player_move_repr = Typewitter.input(message_player_move_repr,
                                            Typewitter.QUESTION)
        if not player_move_repr:
            player_move_repr = player_move_repr_auto

        players.append(Player(player_name, player_move_repr))

    arguments['players'] = players

    play(**arguments)
