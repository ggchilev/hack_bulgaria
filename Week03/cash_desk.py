class Bill:

    def __init__(self, ammount):
        self.ammount = ammount

    def __str__(self):
        return "Money "+str(self.ammount)+" dollars"

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

print(int(a))
print(str(a))
print(a)
print(a == b)
print(a == c)

money_holder = {}
money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print(money_holder)


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

    def __getitem__(self):
        for bill in self.bills:
            print(bill)

batch = BatchBill([a, b, c])

print(batch.__len__())
print(batch.total())
batch.__getitem__()

class CashDesk:

    def __init__(self):
        self.deskAmount = 0
        self.arr = []

    def take_money(self, money):
        sum_bills = 0
        if type(money) is Bill:
            self.deskAmount += money.ammount
            self.arr.append(money.ammount)
            return money.ammount
        elif type(money) is BatchBill:
            for mon in money.bills:
                self.arr.append(mon.ammount)
                sum_bills += mon.ammount
                self.deskAmount += sum_bills
            return sum_bills

    def total(self):
        return self.deskAmount

    def inspect(self):
        dic = {}
        print("We have a total of "+str(self.deskAmount)+" in the desk")
        print("We have the following count of bills :")
        num = 0 
        n = 0
        for item in self.arr:
            dic[item] = self.arr.count(item)
        return dic


desk = CashDesk()
desk.take_money(batch)
desk.take_money(a)
print(desk.total())
print(desk.inspect())