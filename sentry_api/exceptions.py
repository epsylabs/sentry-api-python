class SentryApiException(Exception):
    def __init__(self, response):
        self.response = response


class SentryApiBadInputException(SentryApiException):
    ...


class SentryApiForbiddenException(SentryApiException):
    ...


class SentryApiResourceNotFoundException(SentryApiException):
    ...


class SentryApiConflictException(SentryApiException):
    ...
