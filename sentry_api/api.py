from typing import Type

from sentry_api.http import BaseHttp, RequestsHttp
from sentry_api.resources import ProjectRulesResource, ProjectsResource, TeamsResource


class SentryApi:
    def __init__(
        self, token: str, endpoint_url: str = "https://sentry.io/api/0/", http_client: Type[BaseHttp] = None
    ) -> None:
        self.http_client = http_client(endpoint_url, token) if http_client else RequestsHttp(endpoint_url, token)

    @property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self.http_client)

    @property
    def project_rules(self) -> ProjectRulesResource:
        return ProjectRulesResource(self.http_client)

    @property
    def teams(self) -> TeamsResource:
        return TeamsResource(self.http_client)
