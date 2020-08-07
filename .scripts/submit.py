#!/usr/bin/env python3

import glob
import json
import os
import sys

import requests
import yaml

# Globals

ASSIGNMENTS     = {}
DREDD_QUIZ_URL  = 'https://dredd.h4x0r.space/quiz/cse-30872-fa20/'
DREDD_QUIZ_MAX  = 3.0
if bool(os.environ.get('DEBUG', False)):
    DREDD_CODE_URL = 'https://dredd.h4x0r.space/debug/cse-30872-fa20/'
else:
    DREDD_CODE_URL = 'https://dredd.h4x0r.space/code/cse-30872-fa20/'
DREDD_CODE_MAX  = 6.0

# Utilities

def add_assignment(assignment, path=None):
    if path is None:
        path = assignment

    if assignment.startswith('exercise'):
        ASSIGNMENTS[assignment] = path

def print_results(results):
    for key, value in sorted(results):
        try:
            print('{:>8} {:.2f}'.format(key.title(), value))
        except ValueError:
            if key in ('stdout', 'diff'):
                print('{:>8}\n{}'.format(key.title(), value))
            else:
                print('{:>8} {}'.format(key.title(), value))

# Submit Functions

def submit_code(assignment, path):
    sources = glob.glob(os.path.join(path, 'program.*')) + glob.glob(os.path.join(path, 'solution.*'))

    if not sources:
        print('No code found (program.*)')
        return 1

    result = 1
    for source in sources:
        print('\nSubmitting {} {} ...'.format(assignment, os.path.basename(source)))
        response = requests.post(DREDD_CODE_URL + assignment, files={'source': open(source)})
        print_results(response.json().items())

        result = min(result, 0 if response.json().get('score', 0) >= DREDD_CODE_MAX else 1)
    return result

# Main Execution

# Add GitLab/GitHub branch
for variable in ['CI_BUILD_REF_NAME', 'GITHUB_HEAD_REF']:
    try:
        add_assignment(os.environ[variable])
    except KeyError:
        pass

# Add local git branch
try:
    add_assignment(os.popen('git symbolic-ref -q --short HEAD 2> /dev/null').read().strip())
except OSError:
    pass

# Add current directory
add_assignment(os.path.basename(os.path.abspath(os.curdir)), os.curdir)

# For each assignment, submit quiz answers and program code

if not ASSIGNMENTS:
    print('Nothing to submit!')
    sys.exit(1)

exit_code = 0

for assignment, path in sorted(ASSIGNMENTS.items()):
    print('Submitting {} assignment ...'.format(assignment))
    if 'exercise' in assignment:
        exit_code += submit_code(assignment, path)

sys.exit(exit_code)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
