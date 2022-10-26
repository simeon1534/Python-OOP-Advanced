from account import Account
import unittest


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.acc1 = Account('bob', 10)
        self.acc2 = Account('john')

    def test_adding_tansaction_integer_to_list_transactions(self):
        self.acc1.add_transaction(10)
        self.assertEqual(self.acc1._transactions, [10])

    def test_adding_transaction_not_integer_to_list_transactions(self):
        with self.assertRaises(ValueError):
            self.acc1.add_transaction(10.0)

    def test_showing_balance(self):
        self.acc1.add_transaction(-10)
        self.assertEqual(self.acc1.balance, 0)

    def test_validating_transaction_when_zero_or_positive_balance(self):
        validation = Account.validate_transaction(self.acc1, -10)
        self.assertEqual(validation, f"New balance: 0")

    def test_validating_transaction_when_negative_balance(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.acc1, -11)

    def test_number_of_transactions(self):
        self.acc1.add_transaction(-10)
        self.assertEqual(len(self.acc1._transactions), 1)

    def test_indexing_from_transaction_list(self):
        self.acc1.add_transaction(10)
        self.acc1.add_transaction(20)
        self.acc1.add_transaction(30)
        self.assertEqual(self.acc1._transactions[2], 30)

    def testing_repr_method(self):
        self.assertEqual(repr(self.acc1), f"Account"
                                          f"(bob, 10)")

    def testing_str_method(self):
        self.assertEqual(str(self.acc1), f"Account of bob "
                                         f"with starting amount: 10")

    def testing_comparison_of_balances_of_different_owners(self):
        self.acc3 = Account('rob', 10)
        self.assertTrue(self.acc1 > self.acc2)
        self.assertTrue(self.acc1 == self.acc3)

    def test_adding_acc1_to_acc2_and_creating_new_account_logic(self):
        self.acc1.add_transaction(10)
        self.acc2.add_transaction(-40)
        acc3 = self.acc1 + self.acc2
        self.assertEqual(str(acc3), f"Account of bob&john "
                                    f"with starting amount: 10")
        self.assertEqual(acc3._transactions, [10, -40])


if __name__ == '__main__':
    unittest.main()
