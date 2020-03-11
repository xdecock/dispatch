from starlette.datastructures import URL

from dispatch.config import config, Secret


GITLAB_BROWSER_URL = config("GITLAB_BROWSER_URL", cast=URL)
GITLAB_API_URL = config("GITLAB_API_URL", cast=URL)
GITLAB_AUTH_KEY = config("GITLAB_AUTH_KEY", cast=Secret)
GITLAB_INCIDENT_PROJECT_ID = config("GITLAB_ROJECT_ID")

GITLAB_LABEL_PRIORITY_INFO = config("GITLAB_LABEL_PRIORITY_INFO")
GITLAB_LABEL_PRIORITY_LOW = config("GITLAB_LABEL_PRIORITY_LOW")
GITLAB_LABEL_PRIORITY_MEDIUM = config("GITLAB_LABEL_PRIORITY_MEDIUM")
GITLAB_LABEL_PRIORITY_HIGH = config("GITLAB_LABEL_PRIORITY_HIGH")
GITLAB_LABEL_PRIORITY_VULNERABILITY = config("GITLAB_LABEL_PRIORITY_VULNERABILITY")
