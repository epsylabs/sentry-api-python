from typing import Type

from sentry_api.http import BaseHttp, RequestsHttp
from sentry_api.resources import Projects, Teams


class SentryApi:
    def __init__(
            self,
            token: str,
            endpoint_url: str = "https://sentry.io/api/0/",
            caller: Type[BaseHttp] = None
    ) -> None:
        self.caller = caller(endpoint_url, token) if caller else RequestsHttp(endpoint_url, token)

    @property
    def projects(self) -> Projects:
        return Projects(self.caller)

    @property
    def teams(self) -> Teams:
        return Teams(self.caller)
