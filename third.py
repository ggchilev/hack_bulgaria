def count_words(arr):
    dic = {}
    num = 0
    for i in range(0, len(arr)):
        el = arr[i]
        for element in arr:
            if element == el:
                num += 1
        dic[el] = num
        num = 0
    return dic

# print(count_words(["apple", "banana", "apple", "pie"]))


def nan_expand(times):

    expansion = ""
    if times == 0:
        return ""
    else:
        for i in range(0, times):
            expansion += "Not a "
        expansion += "NaN"
        return expansion


# print(nan_expand(2))

def iterations_of_nan_expand(expanded):

    num = 0
    str = ""
    for i in range(0, len(expanded)):
        str += expanded[i]
        if str == "Not a ":
            num += 1
            str = ""
    return num

# print(iterations_of_nan_expand("Not a Not a Not a Not a NaN"))


def group(list):

    smallGroupList = [list[0]]
    groupList = []
    for i in range(0, len(list) - 1):
        if list[i] == list[i + 1]:
            smallGroupList.append(list[i + 1])
            if i == len(list) - 2:
                groupList.append(smallGroupList)
        else:

            if i == len(list) - 2:
                groupList.append(smallGroupList)
                smallGroupList = []
                smallGroupList.append(list[i + 1])
                groupList.append(smallGroupList)
                break
            groupList.append(smallGroupList)
            smallGroupList = []
            smallGroupList.append(list[i + 1])

    return groupList

# print(group([1, 1, 1, 2, 3, 1, 1, 2]))


def max_consecutive(items):
    length = 0
    arr = group(items)
    for item in arr:
        if len(item) > length:
            length = len(item)
    return length

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))


def gas_stations(distance, tank_size, stations):

    arr = []
    default = tank_size
    if tank_size < stations[0]:
        return "Izgasna po putq"

    for i in range(0, len(stations)):
        if i == 0:
            tank_size = tank_size - stations[i]
            if tank_size < stations[i + 1] - stations[i]:
                tank_size = default
                arr.append(stations[i])
            # print(tank_size)
        else:
            road = stations[i] - stations[i - 1]
            tank_size = tank_size - (stations[i] - stations[i - 1])
            # print(tank_size)
            if tank_size <= road:
                tank_size = default
                arr.append(stations[i])
    return arr

# print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


def sum_of_numbers(st):

    varSum = 0
    number = ""
    for i in range(0, len(st)):
        if st[i].isdigit():
            number += st[i]
            # print(number)
            if i == len(st) - 1:
                varSum += int(number)
        else:
            if number.isdigit():
                varSum = varSum + int(number)
            number = ""
    return varSum

# print(sum_of_numbers("3ab2"))


def numbers_to_message(pressedSequence):

    output = ""
    txt = ""
    is_one = False
    arr = group(pressedSequence)
    keyboard = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
                6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz", 0: " "}
    for item in arr:
        length = len(item) - 1
        for symbol in keyboard:
            if 1 in item:
                is_one = True
                break
            if symbol in item:
                for i in item:
                    length = len(item) - 1 - len(keyboard[symbol])
                if is_one == True:
                    txt += ((keyboard[symbol])[length]).upper()
                    is_one = False
                else:
                    txt += (keyboard[symbol])[length]
                output += txt
                txt = ""
    return output

#print(numbers_to_message(
#    [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(messege):
    arr = []
    keyboard = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
                6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz", 0: " "}
    for symbol in messege:
        for item in keyboard:
            if symbol.isupper():
                arr.append(1)
                symbol = symbol.lower()
            if symbol in keyboard[item]:
                for index in range(0,len(keyboard[item])):
                    if symbol == (keyboard[item])[index]:
                        arr.append(item)
                        break
                    else:
                        if symbol != (keyboard[item])[index]:
                            arr.append(item)
        if not " " in messege: 
            arr.append(-1)
    if not " " in messege:
        return arr[0:len(arr)-1]
    else:
        return arr

#print(message_to_numbers("abc a"))
