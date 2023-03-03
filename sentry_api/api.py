import os
from typing import Type

from sentry_api.exceptions import SentryApiException
from sentry_api.http import BaseHttp, RequestsHttp
from sentry_api.resources import ProjectRulesResource, ProjectsResource, TeamsResource


class SentryApi:
    def __init__(
        self,
        organization_slug: str,
        token: str = None,
        endpoint_url: str = "https://sentry.io/api/0/",
        http_client: Type[BaseHttp] = None,
    ) -> None:
        self.organization_slug = organization_slug

        token = token if token else os.environ.get("SENTRY_TOKEN")

        if not token:
            raise SentryApiException("No token provided. Check https://docs.sentry.io/api/auth/")

        self.http_client = http_client(endpoint_url, token) if http_client else RequestsHttp(endpoint_url, token)

    @property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self.organization_slug, self.http_client)

    @property
    def project_rules(self) -> ProjectRulesResource:
        return ProjectRulesResource(self.organization_slug, self.http_client)

    @property
    def teams(self) -> TeamsResource:
        return TeamsResource(self.organization_slug, self.http_client)
