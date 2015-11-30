from datetime import datetime
import json


def meal(command):

    if "meal" in command:
        return command[0:4]


def list(command):
    if "list" in command:
        return command[0:4]


def list_foods(filename, command):
    food = ""
    with open(filename, 'r') as data:
        for line in data:
            line = line.rstrip('\n')
            if str(command[5:]) in str(line):
                for index in range(0, len(line)):
                    if not line[index].isdigit():
                        food += line[index]
                    else:
                        print(food)
                        food = ""
                        break


def open_json(filename_calories):

    with open(filename_calories, 'r') as f:
        calories = json.load(f)

    return calories


def write_to_json(filename_calories, cals, command):

    calories = open_json(filename_calories)
    dic = {command[5:]: int(cals)}
    calories.update(dic)

    with open(filename_calories, 'w') as f:
        json.dump(calories, f)

    return calories


def info(command, calories):
    your_food = ""
    your_calories = 0
    cal_command = input('How much ' + command[5:] + ' have you eaten>')
    for item in cal_command:
        if item.isdigit():
            your_food += item
    if 'kg' in cal_command:
        your_calories = calories[command[5:]] * int(your_food) * 10
        print('Okay, this is total ' +
              str(your_calories) + ' calories for this meal')
    elif 'g' in cal_command:
        your_calories = calories[command[5:]] * int(your_food) / 100
        print('Okay, this is total ' +
              str(your_calories) + ' calories for this meal')
    else:
        print('use g or kg to see information about calories')


def add_info(filename_calories, command, calories):
    print('I do not have ' + command[5:] + ' in the calories database>')
    cals = input('How much calories per 100g?>')
    calories = write_to_json(filename_calories, cals, command)
    info(command, calories)


def check_calories(filename_calories, command):
    calories = open_json(filename_calories)
    # for food in calories:
    if command[5:] in calories:
        info(command, calories)
    if command[5:] not in calories:
        add_info(filename_calories, command, calories)


def menu():

    print("""
          Hello and Welcome!
          Choose an option.
          1. meal - to write what are you eating now.
          2. list <dd.mm.yyyy> - lists all the meals that you ate that day,""")
    filename = 'panda.txt'
    filename_calories = 'calories.json'
    command = ""
    while True:
        command = input("Enter command>")
        if str(meal(command)) in str(command):
            data = open(filename, 'a')
            data.write(
                command[5:] + " " + str(datetime.now().strftime("%d.%m.%Y")) + "\n")
            check_calories(filename_calories, command)
            data.close()
        elif str(list(command)) in str(command):
            print(list_foods(filename, command))
        else:
            print("Bye")
            break


print(menu())
