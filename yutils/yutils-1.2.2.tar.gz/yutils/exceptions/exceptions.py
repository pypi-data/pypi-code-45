#!%PYTHON_HOME%\python.exe
# coding: utf-8
# version: python37


class YutilsException(Exception):
    pass


# ###############################
# ####### IMPLEMENTATIONS #######
# ###############################


class WrongDatatype(YutilsException):
    """
    Gets raised when something isn't the right datatype as was expected
    """
    _STRING = "Error with '{name}': expected '{expectation}', got '{reality}'"

    def __init__(self, name, expectation, reality):
        """
        :param name: object name
        :type name: str/unicode
        :param expectation: expected type
        :type expectation: type or str/unicode
        :param reality: the object's actual type
        :type reality: type or str/unicode
        """
        super(WrongDatatype, self).__init__(
            self._STRING.format(
                name=name,
                expectation=expectation.__name__ if isinstance(expectation, type) else str(expectation),
                reality=reality.__name__ if isinstance(reality, type) else str(reality)
            )
        )


class WrongInputDatatype(WrongDatatype):
    """
    Gets raised when an input argument isn't the right datatype as was expected
    """
    _STRING = "Error with input '{name}': expected '{expectation}', got '{reality}'"


class MissingAttribute(YutilsException):
    """
    Gets raised when an attribute was expected in a certain class
    """
    _STRING = "Class '{class_name}' doesn't have the expected attribute '{attribute_name}'"

    def __init__(self, class_object, attribute_name):
        """
        :param class_object: the object itself that is missing an attribute
        :type class_object: object
        :param attribute_name: the name of the attribute that is missing
        :type attribute_name: str/unicode
        """
        super(MissingAttribute, self).__init__(
            self._STRING.format(
                class_name=class_object.__name__ if hasattr(class_object, '__name__')
                                               else class_object.__class__.__name__,
                attribute_name=attribute_name
            )
        )


class MissingInput(MissingAttribute):
    """
    Gets raised when an input was expected in a certain class but not received
    """
    _STRING = "Class '{class_name}' didn't receive the expected argument '{attribute_name}'"


class InputError(YutilsException):
    """
    Gets raised when the input wasn't as expected (e.g. isn't a valid option)
    """
    def __init__(self, error_string):
        """
        :param error_string: an error message explaining the InputError
        :type error_string: str/unicode
        """
        super(InputError, self).__init__(error_string)


class CodeMistake(YutilsException):
    """
    Gets raised to find mistakes when writing code
    """
    def __init__(self, mistake_string):
        """
        :param mistake_string: an error message explaining why this was raised
        :type mistake_string: str/unicode
        """
        super(CodeMistake, self).__init__(mistake_string)


class UncaughtEndCase(YutilsException):
    """
    Gets raised to catch unexpected cases in the future
    """
    _DEFAULT_STR = 'An uncaught end case was found. Check it out!'

    def __init__(self, explanation=None):
        """
        :param explanation: an optional string to explain the end case.
                            Default: 'An uncaught end case was found. Check it out!'
        :type explanation: str/unicode
        """
        super(UncaughtEndCase, self).__init__(explanation if explanation else self._DEFAULT_STR)


class UserCancellation(YutilsException):
    """
    Gets raised when a user chooses to cancel an operation, and you wish the program to abort.
    """
    _STRING = "User cancelled operation{operation_description}; Program aborting."
    _DELIMITER = ": '{operation_name}'"

    def __init__(self, operation_name=None):
        """
        :param operation_name: (optional) the operation the user chose to cancel
        :type operation_name: (optional) str/unicode
        """
        super(UserCancellation, self).__init__(
            self._STRING.format(
                operation_description='' if not operation_name else self._DELIMITER.format(operation_name=operation_name)
            )
        )
