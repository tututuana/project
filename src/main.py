#!/bin/python3
import os, subprocess, json, sys

username = 'BetaPictoris'
email = 'git@mrhallway.me'

try:
    job = sys.argv[1]
except:
    print('Invalid.')
    sys.exit()

try:
    working = sys.argv[2]
    lang = sys.argv[3]
except:
    pass

def clone(repo):
    os.system('git clone https://github.com/' + repo + ' .')
    os.system('rm -rf .git')
    os.system('git config user.name ' + username)
    os.system('git config user.email ' + email)
    os.system('git init')

def init(name, lang='python'):
    try:
        os.mkdir(name)
    except FileExistsError:
        pass

    os.chdir(str(name))

    if lang.lower() == 'python':
        clone('BetaPictoris/python-example')
    elif lang.lower() == 'c++':
        clone('BetaPictoris/cpp-example')

def run(job):
    project = open('project.json', 'r')
    project = json.load(project)
    
    for currJob in project:
        if job == currJob:
            for working in project[job]:
                os.system(working)


if job == 'init':
    init(working, lang=lang)
else:
    run(job=job)