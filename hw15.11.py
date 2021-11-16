class BankAccount:

    def __init__(self, account_id, full_name_owner, balance):
        self.account_id = account_id
        self.full_name_owner = full_name_owner
        self.balance = balance
    def __repr__(self):
            return f'BankAccount({self.account_id}, {self.full_name_owner}, {self.balance})'

    def __eq__(self, other):
        if (self.balance) == (other.balance):
            return True
        else:
            return False

    def __add__(self, other):
        return (self.balance + other.balance)

    def __mul__(self, other):
        return (self.balance * other.balance)


    def __str__(self):
        return f' account id: {self.account_id}, owners name: {self.full_name_owner}, balance:{self.balance} '

account1 = (2586, 'Ben Smith', int('360000'))
account2 = (3697, 'Sarah Smith', int('360000'))
print(account1)
print(account2)
print(account1.__repr__())
print(account2.__repr__())
print('balance1 == balance2', account1 [2]==account2 [2])
print('balance1 + balance2', account1[2] + account2[2])
print('balance1 * balance2', account1[2] * account2[2])


