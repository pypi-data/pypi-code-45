class UnexpectedStatusCodeException(Exception):
    def __init__(self, message, response):
        """ Is raised in case the status code returned from
        weaviate is not handled in the client implementation
        and suggests an error

        Custom code can act on the attributes:
        - status_code
        - json

        :param message: An error message specific to the context,
        in which the error occurred
        :param response: The request response of which the status code was unexpected
        """

        # Set error message
        super().__init__(message+"\t"+str(response.json()))

        self.status_code = response.status_code
        self.json = response.json()


class ThingAlreadyExistsException(Exception):
    pass

class AuthenticationFailedException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ServerError500Exception(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
