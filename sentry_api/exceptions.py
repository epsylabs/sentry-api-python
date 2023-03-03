class SentryApiException(Exception):
    def __init__(self, response=None):
        self.response = response


class SentryApiBadInputException(SentryApiException):
    ...


class SentryApiForbiddenException(SentryApiException):
    ...


class SentryApiResourceNotFoundException(SentryApiException):
    ...


class SentryApiConflictException(SentryApiException):
    ...
