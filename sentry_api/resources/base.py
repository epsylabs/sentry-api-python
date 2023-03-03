from sentry_api.http import BaseHttp


class BaseResource:
    def __init__(self, organization_slug: str, http_client: BaseHttp):
        self.organization_slug = organization_slug
        self.http_client = http_client
