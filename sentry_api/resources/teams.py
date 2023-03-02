from sentry_api.http import BaseHttp


class TeamsResource:
    """
    Sentry API: https://docs.sentry.io/api/teams/
    """

    def __init__(self, http_client: BaseHttp):
        self.http_client = http_client

    def get(self, organization_slug: str, team_slug: str):
        """
        Sentry API: https://docs.sentry.io/api/teams/retrieve-a-team/
        """
        return self.http_client.make_a_call("get", f"teams/{organization_slug}/{team_slug}/")
