#!/bin/python3
import requests

# Configuration
## Git configuration
GIT_NAME = "BetaPictoris"
GIT_EMAIL = "git@mrhallway.me"
GIT_BRANCH = "dev"

## Project Git repo info
CHECK_FOR_UPDATE = True
UPDATE_BRANCH = "master"
UPDATE_REPO = "BetaPictoris/Project"
CURRENT_VER = "1.1-beta"

## Local info
PROJECT_TYPES = {
    "python": {
        "name": "Python",
        "repo": "BetaPictoris/python-example"
    },
    "c++": {
        "name": "C++",
        "repo": "BetaPictoris/cpp-example"
    },
    "java": {
        "name": "Java",
        "repo": "BetaPictoris/java-example"
    },
    "react": {
        "name": "React",
        "repo": "BetaPictoris/react-example"
    },
    "tailwind-react": {
        "name": "Tailwind React",
        "repo": "BetaPictoris/tailwind-react-example"
    },
    "dart": {
        "name": "Dart",
        "repo": "BetaPictoris/dart-example"
    },
    "empty": {
        "name": "Empty",
        "repo": "BetaPictoris/empty-example"
    }
}

GIT_HOSTING = {
    "github": {
        "name": "GitHub",
        "url": "https://github.com"
    },
    "gitlab": {
        "name": "GitLab",
        "url": "https://gitlab.com"
    },
    "bitbucket": {
        "name": "Bitbucket",
        "url": "https://bitbucket.org"
    }
}

# TODO: Add more license types
LICENSE_TYPES = {
    "mit": "https://github.com/IQAndreas/markdown-licenses/blob/master/mit.md",
    "bsd-3": "https://github.com/IQAndreas/markdown-licenses/blob/master/bsd-3.md"
}
# ---------------------------------------------

class networkingError(Exception):
    pass

def checkForUpdates():
    URL = "https://raw.githubusercontent.com/" + UPDATE_REPO + "/" + UPDATE_BRANCH + "/version"

    try:
        r = requests.get(URL)
        if r.status_code == 200:
            return r.text
        else:
            raise networkingError("Update URL responded with code " + str(r.status_code) + ",  200.")
    except:
        return networkingError("Request to fetch update URL failed.")


if __name__ == "__main__":
    print(checkForUpdates())