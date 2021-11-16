import shelve

class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'BankAccount id: {self.id}, name: {self.name}, balance: {self.balance} '

account1 = BankAccount(2586, 'Ben Smith', 360000)
print(account1)
account2 = BankAccount(3697, 'Sarah Smith', 760000)
print(account2)
account3 = BankAccount(1470, 'Dan Green', 250000)
print(account3)

sh = shelve.open('Bank Accounts.db')
sh['account1'] = account1.__dict__
account1_from_db = sh['account1']
sh.close()
sh = shelve.open('Bank Accounts.db')
sh['account2'] = account2.__dict__
sh.close()
sh = shelve.open('Bank Accounts.db')
sh['account3'] = account3.__dict__
sh.close()
