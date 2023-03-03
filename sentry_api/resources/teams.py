from .base import BaseResource


class TeamsResource(BaseResource):
    """
    Sentry API: https://docs.sentry.io/api/teams/
    """

    def get(self, team_slug: str):
        """
        Sentry API: https://docs.sentry.io/api/teams/retrieve-a-team/
        """
        return self.http_client.make_a_call("get", f"teams/{self.organization_slug}/{team_slug}/")
