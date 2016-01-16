def sum_of_digits(n):
    sum = 0
    if n > 0:
        while n != 0 or n != -1:
            print(n)
            sum += n % 10
            n = n // 10
        return sum
    else:
        num = str(n)
        for index in range(1, len(num)):
            sum += int(num[index])
        sum *= -1
        return sum


def to_Digits(n):
    arr = []
    if n == 0:
        arr.append(0)
        return arr
    if n < 0:
        n *= -1
    if n > 0:
        while n != 0:
            number = n % 10
            arr.append(number)
            n = n // 10
        return arr[::-1]


def to_Numbers(n):
    number = 0
    for item in n:
        number = (number * 10) + item
    return number


def fact_digits(n):
    sum = 0
    fac = 1

    if n < 0:
        n *= -1

    while n != 0:
        number = n % 10
        for index in range(1, number + 1):
            fac *= index
        sum += fac
        n = n // 10
        fac = 1
    return sum


def fibonacci(n):
    a = 1
    b = 1
    arr = []
    for i in range(0, n):
        arr.append(a)
        temp = a
        a = b
        b = temp + b
    return arr


def fib_number(n):
    a = 1
    b = 1
    number = 0
    for i in range(0, n):
        number = number * 10 + a
        temp = a
        a = b
        b = temp + b
    return number


def palindrome(n):
    st = str(n)
    if st == st[::-1]:
        return True
    else:
        return False


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    number = 0
    for item in str:
        for vowItem in vowels:
            if item == vowItem:
                number += 1
    return number


def count_consonants(str):
    consostants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                   'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    number = 0
    for item in str:
        for consItem in consostants:
            if item == consItem:
                number += 1
    return number


def char_histogram(str):
    map = {}
    num = 0
    index = 0
    index2 = index

    while(index != len(str)):
        item = str[index]

        for index in range(0, len(str)):
            if(str[index] == item):
                num += 1
        map[item] = num
        index = index2 + 1
        index2 += 1
        num = 0
    return map

