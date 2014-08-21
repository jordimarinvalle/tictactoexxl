# -*- coding: utf-8 -*-


class TicTacToeXXLError(Exception):
    '''
    Board custom base exception.

    Keyword arguments:
    message  -- explanation of the error
    '''

    MESSAGE = None

    def __init__(self, message=None):
        error_message = ""
        if self.MESSAGE:
            error_message = self.MESSAGE
        if message:
            error_message = message
        self.parameter = error_message

    def __str__(self):
        return self.parameter
