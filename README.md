<h2 align="center">sentry-api-python</h2>
<p align="center">
<a href="https://pypi.org/project/sentry-api-python/"><img alt="PyPI" src="https://img.shields.io/pypi/v/sentry-api-python"></a>
<a href="https://pypi.org/project/sentry-api-python/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/sentry-api-python.svg"></a>
<a href="https://github.com/epsylabs/sentry-api-python/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/sentry-api-python.svg"></a>
</p>

This project aims to simplify communication with [Sentry REST API](https://docs.sentry.io/api/).

It is in quite early stage, our approach is simple. We cover first endpoints that we use for our tools.
But new PRs are more than welcome.

## Installation

```shell
pip install sentry-api-python
```

## Example of use

### Create project

```python
from sentry_api.api import SentryApi

sentry_api = SentryApi(
    organization_slug="my-org",
    token="<Your Auth Token https://docs.sentry.io/api/auth/>",
)
response = sentry_api.projects.create(
    team_slug="backend",
    project=dict(name="My first project")
)
```

### Create alert with Slack + Linear integration

```python
from sentry_api.api import SentryApi

sentry_api = SentryApi(
    organization_slug="my-org",
    token="<Your Auth Token https://docs.sentry.io/api/auth/>",
    endpoint_url="https://sentry.io/api/0/",
)

response = sentry_api.project_rules.create(
    project_slug="my-first-project",
    rule={
        "name": "Prod issues",
        "owner": "team:<id of team>",
        "environment": "prod",
        "actionMatch": "any",
        "filterMatch": "all",
        "frequency": 10080,  # One week
        "conditions": [
            {"id": "sentry.rules.conditions.first_seen_event.FirstSeenEventCondition"},
            {"id": "sentry.rules.conditions.regression_event.RegressionEventCondition"},
        ],
        "actions": [
            {
                "workspace": "<slack workspace>",
                "id": "sentry.integrations.slack.notify_action.SlackNotifyServiceAction",
                "channel": "#alerts-production",
                "channel_id": "<https://docs.sentry.io/product/integrations/notification-incidents/slack/#rate-limiting-error>",
            },
            {
                "id": "sentry.rules.actions.notify_event_sentry_app.NotifyEventSentryAppAction",
                "sentryAppInstallationUuid": "<app installation here>",
                "settings": [
                    {"name": "teamId", "value": "<linear team id>"},
                    {"name": "assigneeId", "value": ""},
                    {"name": "labelId", "value": "<label id>"},
                    {"name": "projectId", "value": ""},
                    {"name": "stateId", "value": "<state id>"},
                    {"name": "priority", "value": "1"},
                ],
                "hasSchemaFormConfig": True,
            },
        ],
    },
)
print(response.json())
```
