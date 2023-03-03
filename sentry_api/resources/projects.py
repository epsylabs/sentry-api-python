from sentry_api.exceptions import SentryApiConflictException

from .base import BaseResource


class ProjectsResource(BaseResource):
    def get(self, project_slug: str):
        """
        Sentry API: https://docs.sentry.io/api/projects/retrieve-a-project/
        """
        return self.http_client.make_a_call("get", f"projects/{self.organization_slug}/{project_slug}/")

    def create(self, team_slug: str, project: dict):
        """
        If no `project_slug` is passed and you will call this method multiple times with same `project_name`
        multiple projects will be created with different `slug`. It's behaviour of Sentry API.

        If you want to make sure that you do not create duplicated projects, make sure to:
        - pass `project_slug` parameter
        - catch `SentryApiConflictException` exception.

        Sentry API: https://docs.sentry.io/api/teams/create-a-new-project/
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/team_projects.py#L94

        """
        return self.http_client.make_a_call("post", f"teams/{self.organization_slug}/{team_slug}/projects/", project)

    def update(self, project_slug: str, project: dict):
        """
        Sentry API: https://docs.sentry.io/api/projects/update-a-project/
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_details.py#L396
        """

        return self.http_client.make_a_call("put", f"projects/{self.organization_slug}/{project_slug}/", project)

    def upsert(self, team_slug: str, project_slug: str, project: dict):
        """
        Creates new project if didn't exist and updates existing one.

        If project didn't exist it also makes additional call to make sure all attributes passed in `project`
        variable are sent to Sentry endpoint. Because
        """
        try:
            self.create(team_slug, project)
            response = self.update(project_slug, project)
        except SentryApiConflictException:
            response = self.update(project_slug, project)

        return response
