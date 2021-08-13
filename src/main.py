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
    os.system('git clone https://github.com/' + repo + ' . >> /dev/null')
    os.system('rm -rf .git >> /dev/null')
    os.system('git config user.name ' + username + ' >> /dev/null')
    os.system('git config user.email ' + email + ' >> /dev/null')
    os.system('git init >> /dev/null')

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
    elif lang.lower() == 'java':
        clone('BetaPictoris/java-example')
    elif lang.lower() == 'empty':
        clone('BetaPictoris/empty-example')

def run(job):
    project = open('project.json', 'r')
    project = json.load(project)
    
    for currJob in project:
        if job == currJob:
            for working in project[job]:
                if working.startswith('cd'):
                    os.chdir(working.split(' ')[1])
                else:
                    os.system(working + '')
            break

if job == 'init':
    init(working, lang=lang)
else:
    run(job=job)
    