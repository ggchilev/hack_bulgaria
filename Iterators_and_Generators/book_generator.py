from random import choice
from string import ascii_uppercase
from random import randint


def generate_book(chapter_count, chapter_length):
    my_file = open('avtorsko.txt', 'w')
    number = 0
    for index in range(0, chapter_count):
        number += 1
        my_file.write('\n\n' + '#Chapter ' + str(number) + '\n \n')
        for i in range(0, chapter_length):
            num = randint(1, 20)
            my_file.write(''.join(choice(ascii_uppercase) for i in range(num)) + " ")
            if num == 10:
                my_file.write('\n')
    my_file.close()


generate_book(10, 100)
