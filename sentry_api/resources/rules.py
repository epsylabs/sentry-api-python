from sentry_api.http import BaseHttp


class ProjectRulesResource:
    def __init__(self, http_client: BaseHttp):
        self.http_client = http_client

    def all(self, organization_slug: str, project_slug: str):
        """
        Sentry API: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_rules.py#L25
        """
        return self.http_client.make_a_call("get", f"projects/{organization_slug}/{project_slug}/rules/")

    def create(self, organization_slug: str, project_slug: str, rule: dict):
        """
        Sentry API: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_rules.py#L46
        """
        return self.http_client.make_a_call("post", f"projects/{organization_slug}/{project_slug}/rules/", rule)
