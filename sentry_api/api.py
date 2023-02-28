from typing import Type
from urllib.parse import urljoin

import requests


class SentryApiException(Exception):
    def __init__(self, response):
        self.response = response


class SentryApiBadInputException(SentryApiException):
    ...


class SentryApiForbiddenException(SentryApiException):
    ...


class SentryApiResourceNotFoundException(SentryApiException):
    ...


class SentryApiConflictException(SentryApiException):
    ...


class RequestsCaller:
    class BaseUrlSession(requests.Session):
        def __init__(self, base_url=None):
            super().__init__()
            self.base_url = base_url

        def request(self, method, url, *args, **kwargs):
            joined_url = urljoin(self.base_url, url)
            if "json" in kwargs:
                kwargs["json"] = self.remove_empty(kwargs["json"])

            return super().request(method, joined_url, *args, **kwargs)

        def remove_empty(self, params: dict):
            """
            This method removes any parameters that do not have value set.
            So e.g. if we would pass `None` for `slug` during update of project we would get 405 response
            """
            return {k: v for k, v in params.items() if v is not None}

    def __init__(self, endpoint_url: str, token: str) -> None:
        self.session = RequestsCaller.BaseUrlSession(endpoint_url)
        self.session.headers.update({"authorization": "Bearer " + token})

    def make_a_call(self, http_method: str, endpoint: str, data: dict = None):
        r = self.session.request(http_method, endpoint, json=data)

        if r.status_code == 400:
            raise SentryApiBadInputException(r)

        if r.status_code == 403:
            raise SentryApiForbiddenException(r)

        if r.status_code == 404:
            raise SentryApiResourceNotFoundException(r)

        if r.status_code == 405:
            raise SentryApiException(r)

        if r.status_code == 409:
            raise SentryApiConflictException(r)

        return r


class Projects:
    """
    https://docs.sentry.io/api/teams/create-a-new-project/
    """

    def __init__(self, caller: RequestsCaller):
        self.caller = caller

    def create(self, organization_slug: str, team_slug: str, project_name: str, project_slug: str = None):
        """
        If no `project_slug` is passed and you will call this method multiple times with same `project_name`
        multiple projects will be created with different `slug`. It's behaviour of Sentry API.

        If you want to make sure that you do not create duplicated projects, make sure to:
        - pass `project_slug` parameter
        - catch `SentryApiConflictException` exception.

        Sentry: https://docs.sentry.io/api/teams/create-a-new-project/
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
    ):
        """
        Sentry: https://docs.sentry.io/api/projects/update-a-project/
        """
        return self.caller.make_a_call(
            "put",
            f"projects/{organization_slug}/{project_slug}/",
            dict(name=new_project_name, slug=new_project_slug, platform=new_platform, isBookmarked=new_is_bookmarked)
        )


class SentryApi:
    def __init__(
            self,
            token: str,
            endpoint_url: str = "https://sentry.io/api/0/",
            caller: Type[RequestsCaller] = RequestsCaller
    ) -> None:
        self.caller = caller(endpoint_url, token) if caller else RequestsCaller(endpoint_url, token)

    @property
    def projects(self) -> Projects:
        return Projects(self.caller)
