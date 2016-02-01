class BankAccount:


    def __init__(self, name, balance, currency):
        self._name = name
        if balance < 0:
            raise ValueError
        else:
            self._balance = balance
        self._currency = currency

        self.list_history = ["Account was created"]

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self._balance += amount
            self.list_history.append("Deposited " + str(amount) + str(self._currency))
            return amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False

    def get_name(self):
        return self._name

    def balance(self):
        return self._balance

    def get_currency(self):
        return self._currency

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.amount, self.currency)

    def __int__(self):
        return self._balance

    def transfer_to(self, account, amount):
        if self._currency == account._currency:
            account._balance += amount
            my_str = self._name+" transfered "+str(amount)+" dollars to "+account._name
            self.list_history.append(my_str)
            return True
        else:
            return False

    def history(self):
        #self.deposit(100)
        self.list_history.append("Balance check -> " + str(self._balance) + str(self._currency))
        self.list_history.append("__int__ check -> " + str(int(self)) + str(self._currency))
        return self.list_history

a = BankAccount("daw", 21, "$")
print(a.history())
