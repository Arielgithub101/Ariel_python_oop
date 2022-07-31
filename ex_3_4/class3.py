class BankAccount:
    def __int__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self,Depositmony):
        self.balance += Depositmony
        print(f'you have a total of {self.balance} after Deposit')
    def Withdrawal(self,WithdrawalMony):
        self.balance -= WithdrawalMony
        print(f'you have a total of {self.balance} after Withdrawal Mony')
    def bankFees(self):
        print(f'bank fees for the service is {self.balance * 0.05}, thank you!!')
    def display(self):
        print('the total detail of your accunt is :')
        print(f' oner name : {self.name}')
        print(f' accountNumber: {self.accountNumber}')
        print(f'balance :  {self.balance}')
        print(f'bank fees after actions : {self.bankFees()}')