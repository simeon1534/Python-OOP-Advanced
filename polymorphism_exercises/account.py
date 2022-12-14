from typing import List


class Account:
    owner: str
    amount: int
    _transactions: list

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account: 'Account', amount_to_add):
        account.add_transaction(amount_to_add)
        if account.balance + amount_to_add < 0:  # BANKRUPT
            account._transactions.pop(-1)
            raise ValueError("sorry cannot go in debt!")
        return f"New balance: {account.balance}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_transactions = self._transactions + other._transactions
        new_name = self.owner + '&' + other.owner
        new_summed_amount = self.amount + other.amount
        acc = Account(new_name, new_summed_amount)
        acc._transactions = new_transactions
        return acc


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
