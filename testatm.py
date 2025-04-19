import unittest
from atm import atm_withdrawl

class TestATMWithdrawal(unittest.TestCase):
    
    def test_insufficient_funds(self):
        message, new_balance = atm_withdrawl(100, 150)
        self.assertEqual(message, "no suffisient fund")
        self.assertEqual(new_balance, 100)

    def test_invalid_amount(self):
        message, new_balance = atm_withdrawl(100, -20)
        self.assertEqual(message, "invalid number")
        self.assertEqual(new_balance, 100)

    def test_transaction_successful(self):
        message, new_balance = atm_withdrawl(200, 100)
        self.assertEqual(message, "transaction successfull")
        self.assertEqual(new_balance, 100)                                       
if __name__ == "__main__":
    unittest.main()