"""A module that represents the custom exception """


class GameException(Exception):
    """game Exception"""

    def __init__(self, error_message=None, exception=None):
        """Instantiates the game Exceptions with parameters as,
        :param error_message: detailed error message when exception is raised
        :type error_message: str
        :param exception: Exception instance
        :type exception: Exception
        """
        self.exception = exception
        self.error_message = error_message
        super().__init__()

    # string representation of this class object
    def __str__(self):
        """A string representation of exception class
        :returns: a string of error_message
        :rtype: str
        """
        return '%s' % (self.error_message)


class PlayerException(GameException):
    """An exception that represents the player exception"""

    def __init__(self, error_message=None, exception=None):
        """Instantiates the PlayerException Exceptions
        :param error_message: detailed error message when exception is raised
        :type error_message: str
        :param exception: Exception instance
        :type: Exception
        """
        self.error_message = error_message
        self.exception = exception
        super().__init__(error_message=error_message,
                         exception=exception)


class LadderException(GameException):
    """An exception that represents the ladder exception"""

    def __init__(self, error_message=None, exception=None):
        """Instantiates the LadderException Exceptions
        :param error_message: detailed error message when exception is raised
        :type error_message: str
        :param exception: Exception instance
        :type: Exception
        """
        self.error_message = error_message
        self.exception = exception
        super().__init__(error_message=error_message,
                         exception=exception)


class SnakeException(GameException):
    """An exception that represents the snake exception"""

    def __init__(self, error_message=None, exception=None):
        """Instantiates the SnakeException Exceptions
        :param error_message: detailed error message when exception is raised
        :type error_message: str
        :param exception: Exception instance
        :type: Exception
        """
        self.error_message = error_message
        self.exception = exception
        super().__init__(error_message=error_message,
                         exception=exception)


class DiceException(GameException):
    """An exception that represents the dice exception"""

    def __init__(self, error_message=None, exception=None):
        """Instantiates the DiceException Exceptions
        :param error_message: detailed error message when exception is raised
        :type error_message: str
        :param exception: Exception instance
        :type: Exception
        """
        self.error_message = error_message
        self.exception = exception
        super().__init__(error_message=error_message,
                         exception=exception)
