def chain(iterable_one, iterable_two):
    for item in iterable_one:
        yield item
    for item in iterable_two:
        yield item

gen = chain(range(0, 4), range(4, 8))
# for item in gen:
#     print(item)


def compress(iterable, mask):
    for index in range(0, len(iterable)):
        if mask[index] is True:
            yield iterable[index]

gen = compress(["Ivo", "Rado", "Panda"], [False, False, True])
# for i in gen:
#     print(i)


def cycle(iterable):
    while True:
        for item in iterable:
            yield item

gen = cycle(range(0, 10))
# for i in gen:
#     print(i)


def read_books():
    command = ""
    my_file = open('001.txt', 'r')
    for line in my_file:
        if '#' in line:
            break
        yield line


gener = read_books()
for i in gener:
    print(i)
