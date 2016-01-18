class Bill:

    def __init__(self, ammount):
        if type(ammount) is not int:
            raise TypeError
        elif ammount < 0:
            raise ValueError
        else:
            self.ammount = ammount

    def __str__(self):
        return "A " + str(self.ammount) + "$ bill"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.ammount

    def __eq__(self, other):
        return self.ammount == other.ammount

    def __hash__(self):
        return hash(self.ammount)


a = Bill(10)
b = Bill(5)
c = Bill(10)

# print(int(a))
# print(str(a))
# print(a)
#print(a == b)
#print(a == c)

money_holder = {}
money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

# print(money_holder)


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        num = 0
        for item in self.bills:
            num += 1
        return num

    def total(self):
        return sum([bill.ammount for bill in self.bills])

    def __getitem__(self, index):
        return self.bills[index]

batch = BatchBill([a, b, c])

# for bill in batch:
#    print(bill)

# print(batch.__len__())
# print(batch.total())


class CashDesk:

    def __init__(self):
        self.deskAmount = 0
        self.arr = []

    def take_money(self, money):
        sum_bills = 0
        if type(money) is Bill:
            self.deskAmount += money.ammount
            self.arr.append(money)
            return self.deskAmount
        elif type(money) is BatchBill:
            for mon in money.bills:
                self.arr.append(mon)
                self.deskAmount += mon.ammount
            return self.deskAmount

    def da(self):
        for item in self.arr:
            print(item)

    def total(self):
        return self.deskAmount

    def sort_arr(self):
        for index in range(0, len(self.arr)):
            for index in range(0, len(self.arr) - 1):
                if self.arr[index].ammount > self.arr[index + 1].ammount:
                    temp = self.arr[index]
                    self.arr[index] = self.arr[index + 1]
                    self.arr[index + 1] = temp

        return self.arr

    def inspect(self):
        dic = {}
        my_str = "We have a total of " + \
            str(self.deskAmount) + "$ in the desk \n"
        my_str += "We have the following count of bills, sorted in ascending order : \n"
        num = 0
        n = 0
        self.sort_arr()
        for item in self.arr:
            dic[item] = self.arr.count(item)
            if str(item) not in my_str:
                my_str += str(item) + " - " + str(dic[item]) + "\n"
        return my_str


desk = CashDesk()
desk.take_money(batch)
desk.take_money(a)
#print(desk.sort_arr())
#print(desk.total())
#print(desk.inspect())
