from sentry_api.http import BaseHttp


class ProjectsResource:
    def __init__(self, http_client: BaseHttp):
        self.http_client = http_client

    def get(self, organization_slug: str, project_slug: str):
        """
        Sentry API: https://docs.sentry.io/api/projects/retrieve-a-project/
        """
        return self.http_client.make_a_call("get", f"projects/{organization_slug}/{project_slug}/")

    def create(self, organization_slug: str, team_slug: str, project: dict):
        """
        If no `project_slug` is passed and you will call this method multiple times with same `project_name`
        multiple projects will be created with different `slug`. It's behaviour of Sentry API.

        If you want to make sure that you do not create duplicated projects, make sure to:
        - pass `project_slug` parameter
        - catch `SentryApiConflictException` exception.

        Sentry API: https://docs.sentry.io/api/teams/create-a-new-project/
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/team_projects.py#L94

        """
        return self.http_client.make_a_call("post", f"teams/{organization_slug}/{team_slug}/projects/", project)

    def update(self, organization_slug: str, project_slug: str, project: dict):
        """
        Sentry API: https://docs.sentry.io/api/projects/update-a-project/
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_details.py#L396
        """

        return self.http_client.make_a_call("put", f"projects/{organization_slug}/{project_slug}/", project)
