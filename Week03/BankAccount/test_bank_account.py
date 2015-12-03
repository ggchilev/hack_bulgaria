import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount("Sasho", 100, "dollars")
        self.acc2 = BankAccount("Misho", 200, "dollars")

    def test_init(self):
        self.assertEqual(self.acc.get_name(), "Sasho")
        self.assertEqual(self.acc.get_balance(), 100)
        self.assertEqual(self.acc.get_currency(), "dollars")

    def test_deposits(self):
        self.acc.deposit(200)
        self.assertEqual(self.acc.get_balance(), 300)

    def test_withdraw(self):
        self.acc.withdraw(100)
        self.assertEqual(self.acc.get_balance(), 0)

    def test_transfer(self):
        self.acc.transfer_to(self.acc2, 100)
        self.assertEqual(self.acc2.get_balance(), 300)

    def test_history(self):
        arr2 = self.acc.history(self.acc2, 50)
        arr = ["Account was created", "Balance : "+str(self.acc.get_balance()), "Sasho transfered 50 dollars to Misho", "Balance : 100"]
        self.assertEqual(arr, arr2)





if __name__ == '__main__':
    unittest.main()
