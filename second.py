from copy import deepcopy


def is_number_balanced(n):
    leftSum = 0
    rightSum = 0
    if n % 10 == n:
        return True
    else:
        arr = []
        while n != 0:
            arr.append(n % 10)
            n = n // 10
        print(arr)
        if(len(arr) % 2 == 0):
            print(len(arr))
            return False
        else:
            lastIndex = len(arr)
            middle = (int)(len(arr) / 2)
            print(middle)
            for index in range(0, middle):
                leftSum += arr[index]
            print(leftSum)
            for index2 in range(middle + 1, len(arr)):
                rightSum += arr[index2]
            print(rightSum)
            if(leftSum == rightSum):
                return True
            else:
                return False


def is_increasing(seq):

    for index in range(0, len(seq) - 1):
        if len(seq) == 1:
            return True
        elif (seq[index] > seq[index + 1]):
            return False
    return True


def is_decreasing(seq):
    if len(seq) == 1:
        return True
    for index in range(0, len(seq) - 1):

        if (seq[index] < seq[index + 1]):
            return False
    return True


def get_largest_palindrome(n):

    for index in range(n - 1, 0, -1):
        num = str(index)
        revNum = num[::-1]
        print(num + "  " + revNum)
        if num == revNum:
            return num
    return n


def prime_numbers(n):
    list = []
    isPrime = True
    for index in range(n, 1, -1):
        for index2 in range(2, index):
            if index % index2 == 0:
                print(index2)
                isPrime = False
                break
        if isPrime == True:
            list.append(index)
        isPrime = True
    return list


def is_anagram(a, b):
    num = 0
    if len(a) != len(b):
        return False
    else:
        for index in range(0, len(a)):
            if a[index].upper() in b.upper():
                num += 1
        if num == len(b):
            return True
        else:
            return False


def birthday_ranges(birthdays, ranges):
    list = []

    for rang in ranges:
        num = 0

        for day in birthdays:
            if day in range(rang[0], rang[1] + 1):
                num += 1

        list.append(num)

    return list

#print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15],[(4, 9), (6, 7), (200, 225), (300, 365)]))


def sum_matrix(m):
    sum = 0
    for item in m:
        for i in item:
            sum += i
    return sum

def matrix_bombing_plan(m):

    row = 0
    col = 0
    rows = 3
    cols = 3
    sum = 0
    dic = {}
    n = deepcopy(m)
    print(n)
    print(m)
    for j in range(0, rows * cols):
        bomb = n[row][col]
        for item in range(0, rows):
            for i in range(0, cols):
                if (item == row + 1 and (i == col or i == col + 1 or i == col - 1)) or (item == row and (i == col + 1 or i == col - 1)) or (item == row - 1 and (i == col - 1 or i == col or i == col + 1)):
                    if n[item][i] - bomb > 0 and n[item][i] != bomb:
                        n[item][i] -= bomb
                    else:
                        if n[item][i] != bomb:
                            n[item][i] = 0
                print(n[item][i], bomb)
                sum += n[item][i]
        dic[(row, col)] = sum
        sum = 0
        if col != 2:
            col += 1
        else:
            col = 0
            row += 1
        n = deepcopy(m)
        print(m)
    return dic

# print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def is_transversal(transversal, family):
    
    if len(transversal) != len(family):
        return False

    number = 0
    for fam in family:
        for item in fam:
            if item in transversal:
                number += 1
        if number == 0 or number > 1:
            return False
        number = 0
    return True

print(is_transversal([2, 3, 4], [[1, 7], [2, 3, 5], [4, 8]]))
