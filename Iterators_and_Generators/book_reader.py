class Iterator:

    def __next__(self, *args):
        books_list = self.books('avtorsko.txt')
        for item in books_list:
            FILE = open(item, 'r')
            for line in FILE:
                if '#' in line:
                    input('Press Enter to continue')
                yield line

    def __iter__(self):
        return self

    def books(self, *args):
        books_list = []
        for item in args:
            books_list.append(item)
        return books_list


iterator = Iterator()
it = next(iterator)
for i in it:
    print(i)
