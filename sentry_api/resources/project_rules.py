from .base import BaseResource


class ProjectRulesResource(BaseResource):
    def all(self, project_slug: str):
        """
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_rules.py#L25
        """
        return self.http_client.make_a_call("get", f"projects/{self.organization_slug}/{project_slug}/rules/")

    def create(self, project_slug: str, rule: dict):
        """
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_rules.py#L46
        """
        return self.http_client.make_a_call("post", f"projects/{self.organization_slug}/{project_slug}/rules/", rule)

    def update(self, project_slug: str, rule_id: int, rule: dict):
        """
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_rule_details.py#L85
        """
        return self.http_client.make_a_call(
            "put",
            f"projects/{self.organization_slug}/{project_slug}/rules/{rule_id}/",
            rule
        )
