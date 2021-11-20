#!/bin/python3
import requests
import sys
import json
import os

# Configuration
PROJECT_CONFIG = "project.json"

## Git configuration
GIT_NAME = "BetaPictoris"
GIT_EMAIL = "git@mrhallway.me"
GIT_BRANCH = "dev"

## Project Git repo info
CHECK_FOR_UPDATES = True
UPDATE_BRANCH = "beta"
UPDATE_REPO = "BetaPictoris/project"
CURRENT_VER = "1.1.2-" + UPDATE_BRANCH

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
    "bsd-2": "https://github.com/IQAndreas/markdown-licenses/blob/master/bsd-2.md",
    "bsd-3": "https://github.com/IQAndreas/markdown-licenses/blob/master/bsd-3.md",

    "gnu-gpl-v3.0": "https://github.com/IQAndreas/markdown-licenses/blob/master/gnu-lgpl-v3.0.md",

    "unlicense": "https://github.com/IQAndreas/markdown-licenses/blob/master/unlicense.md"
}
# ---------------------------------------------

# SETUP
## Errors
class networkingError(Exception):
    pass

class projectTypeError(Exception):
    pass

class buildError(Exception):
    pass

class projectNull(Exception):
    pass

## Help message text
HELP_MSG = """
Project by Beta Pictoris - version """ + CURRENT_VER + """

info - Get information about the project
update - Update the project file
init - Initialize a new project
build - Build the project
help - Get this help message"""

# UPDATES
def checkForUpdates():
    URL = "https://raw.githubusercontent.com/" + UPDATE_REPO + "/" + UPDATE_BRANCH + "/version"

    try:
        r = requests.get(URL)
        if r.status_code == 200:
            return r.text
        else:
            raise networkingError("Update URL responded with code " + str(r.status_code) + ".")
    except:
        return networkingError("Request to fetch update URL failed.")

def updateProject():
    if CURRENT_VER != checkForUpdates():
        clone(UPDATE_REPO, dest="update", host="github")
# MAIN FUNCTIONS
def runJob(job):
    os.system(job)

def clone(repo, dest, host="github"):
    os.mkdir(dest)
    os.chdir(dest)
    os.system("git clone " + GIT_HOSTING[host]['url'] + "/" + repo + " .")

def readProjectConfig():
    try:
        f = open(PROJECT_CONFIG, "r")
        data = f.read()
        jsonData = json.loads(data)
        f.close()

        return jsonData
    except:
        raise projectNull("Project configuration file is missing or broken.")

def getInfo():
    jsonData = readProjectConfig()

    print("Project name: " + jsonData["name"])
    print("Description: " + jsonData["license"])
    print("License: " + jsonData["license"])
    print("Version: " + jsonData["version"])

def initProject(projectName, projectType, host="github"):
    if projectType in PROJECT_TYPES:
        url = PROJECT_TYPES[projectType]["repo"]
    else:
        url = GIT_HOSTING[host]["url"] + "/" + projectType
    
    clone(url, dest=projectName, host=host)

def buildProject(task="run"):
    jsonData = readProjectConfig()

    tasksListing = jsonData["build"]

    if task in tasksListing:
        jobs = tasksListing[task]

        for currentJob in jobs:
            runJob(currentJob)
    else:
        raise buildError("Invalid build task.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(HELP_MSG)
        sys.exit()

    if CHECK_FOR_UPDATES:
        try:
            REMOTE_VERSION = checkForUpdates()
        except networkingError as e:
            print(e)
            sys.exit()
        
        if REMOTE_VERSION != CURRENT_VER:
            print("Update available!\nCurrent: " + CURRENT_VER + "\nRemote: " + REMOTE_VERSION)
            check = input("Update right now? (Y/n) ")
            if check == "Y" or check == "y" or check == "":
                updateProject()
        else:
            pass
    
    if sys.argv[1] == "info":
        getInfo()
    elif sys.argv[1] == "init":
        try:
            if len(sys.argv) == 4:
                initProject(sys.argv[2], sys.argv[3], sys.argv[4])
            elif len(sys.argv) == 3:
                initProject(sys.argv[2], sys.argv[3])
        except projectNull as e:
            print(e)
            sys.exit()
        except IndexError:
            print("Project name and type are required.")
            sys.exit()
    elif sys.argv[1] == "update":
        updateProject()
    elif sys.argv[1] == "build":
        try:
            if len(sys.argv) == 2:
                buildProject()
            else:
                buildProject(sys.argv[2])
        except buildError as e:
            print(e)
            sys.exit()
    else:
        print(HELP_MSG)
