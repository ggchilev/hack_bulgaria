import json
import sys

def open_json():
    with open(sys.argv[1], 'r') as f:
        people = json.load(f)

    return people

def language_level(levels):
    people = open_json()
    for person in people['people']:
        for skill in person['skills']:
            levels[skill['name']] = skill['level']

    return levels

def language_name(best_programmers):
    people = open_json()
    for person in people['people']:
        for skill in person['skills']:
            best_programmers[skill['name']] = person['first_name']

    return best_programmers


def programmers():


    levels = {}
    best_programmers = {}
    
    people = open_json()
    levels = language_level(levels)
    best_programmers = language_name(best_programmers)

    for person in people['people']:
        for skill in person['skills']:
            for item in levels:
                if item == skill['name']:
                    if skill['level'] > levels[item]:
                        levels[item] = skill['level']
                        best_programmers[skill['name']] = person['first_name']


    return best_programmers


print(programmers())
