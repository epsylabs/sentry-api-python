class SentryApiException(Exception):
    def __init__(self, msg):
        self.msg = msg


class SentryApiHttpException(SentryApiException):
    def __init__(self, response):
        self.response = response


class SentryApiBadInputException(SentryApiHttpException):
    ...


class SentryApiForbiddenException(SentryApiHttpException):
    ...


class SentryApiResourceNotFoundException(SentryApiHttpException):
    ...


class SentryApiConflictException(SentryApiHttpException):
    ...


class SentryApiNoTokenProvidedException(SentryApiException):
    ...
