from sentry_api.http import BaseHttp


class Teams:
    """
    Sentry API: https://docs.sentry.io/api/teams/
    """

    def __init__(self, caller: BaseHttp):
        self.caller = caller

    def get(self, organization_slug: str, team_slug: str):
        """
        Sentry API: https://docs.sentry.io/api/teams/retrieve-a-team/
        """
        return self.caller.make_a_call("get", f"teams/{organization_slug}/{team_slug}/")


class Projects:
    def __init__(self, caller: BaseHttp):
        self.caller = caller

    def get(self, organization_slug: str, project_slug: str):
        """
        Sentry API: https://docs.sentry.io/api/projects/retrieve-a-project/
        """
        return self.caller.make_a_call(
            "get",
            f"projects/{organization_slug}/{project_slug}/"
        )

    def create(self, organization_slug: str, team_slug: str, project_name: str, project_slug: str = None):
        """
        If no `project_slug` is passed and you will call this method multiple times with same `project_name`
        multiple projects will be created with different `slug`. It's behaviour of Sentry API.

        If you want to make sure that you do not create duplicated projects, make sure to:
        - pass `project_slug` parameter
        - catch `SentryApiConflictException` exception.

        Sentry API: https://docs.sentry.io/api/teams/create-a-new-project/

        """
        return self.caller.make_a_call(
            "post",
            f"teams/{organization_slug}/{team_slug}/projects/",
            dict(name=project_name, slug=project_slug)
        )

    def update(
            self,
            organization_slug: str,
            project_slug: str,
            new_project_name: str = None,
            new_project_slug: str = None,
            new_platform: str = None,
            new_is_bookmarked: bool = None,
            new_resolve_age: int = None,
    ):
        """
        Sentry API: https://docs.sentry.io/api/projects/update-a-project/
        Sentry API Code: https://github.com/getsentry/sentry/blob/master/src/sentry/api/endpoints/project_details.py#L396
        """

        return self.caller.make_a_call(
            "put",
            f"projects/{organization_slug}/{project_slug}/",
            dict(name=new_project_name, slug=new_project_slug, platform=new_platform, isBookmarked=new_is_bookmarked, resolveAge=new_resolve_age)
        )

    def list_rules(self, organization_slug: str, project_slug: str):
        ...
