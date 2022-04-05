class BankAccount:

    balance = 0
    interest = .02
    accounts = []

    def __init__(self, intRate = interest, bal = balance):
        self.intRate = intRate
        self.balance = bal
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds: charging a $5 fee')
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def displayAccountInfo(self):
        print(f'Account:  Balance: ${self.balance}')

    def yieldInterest(self):
        if self.balance > 0:
            sum = self.balance * self.intRate
            self.balance += sum
            return self
        else:
            return self

    @classmethod
    def bankAccountInfo(cls):
        for i in cls.accounts:
            print(i.balance, i.intRate)


class user:
    def __init__(self, firstName, lastName, accNum = 1):
        self.firstName = firstName
        self.lastName = lastName
        self.accounts = []
        for i in range(0, accNum):
            self.accounts.append(BankAccount())
            i += 1
        

    def makeDeposit(self, amount, accNum = 0):
        self.accounts[accNum].balance += amount
        return self

    def makeWithdrawal(self, amount, accNum = 0):
        self.accounts[accNum].balance -= amount
        return self

    def displayUserBalance(self, accNum = 0):
        print(f'User: {self.firstName} {self.lastName} - Balance {self.accounts[accNum].balance}.')

    def transfer(self, amount, targetAcc, accNum = 0):
        self.accounts[accNum].balance -= amount
        targetAcc.accounts[accNum].balance += amount
        print(self.accounts[accNum].balance)
        print(targetAcc.accounts[accNum].balance)


bob = user('Bob', 'Smith')
tommy = user('Tommy', 'Timber', 2)
jimmy = user('Jimmy', 'Johnson')

bob.makeDeposit(100).makeDeposit(100).makeDeposit(100).makeDeposit(100).makeWithdrawal(25).displayUserBalance()

tommy.makeDeposit(100, 0).makeDeposit(100, 1).makeWithdrawal(25, 0).makeWithdrawal(25, 1).displayUserBalance(1)
tommy.displayUserBalance(0)

jimmy.makeDeposit(100).makeWithdrawal(25).makeWithdrawal(25).makeWithdrawal(25).displayUserBalance()

bob.transfer(100, jimmy)