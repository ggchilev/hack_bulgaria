class BankAccount:


    def __init__(self, name, balance, currency):
        self._name = name
        if balance < 0:
            raise ValueError
        else:
            self._balance = balance
        self._currency = currency

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self._balance += amount
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
        return self.balance

    def transfer_to(self, account, amount):
        if self._currency == account._currency:
            account._balance += amount
            return True
        else:
            return False

    def history(self, account, amount):
        list_history = ["Account was created", "Balance : "+str(self._balance)]
        if self.transfer_to(account, amount) == True:
            list_history.append(self._name+" transfered "+str(amount)+" dollars to "+account._name)
            list_history.append("Balance : "+str(self._balance))
        return list_history


