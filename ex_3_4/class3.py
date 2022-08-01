class BankAccount:
    def __int__(self, accountNumber: int, name:str, balance: int):
        self.accountNumber:int = accountNumber
        self.name: str= name
        self.balance:int = balance
    def deposit(self,Depositmony:int):
        self.balance += Depositmony
        print(f'you have a total of {self.balance} after Deposit')
    def withdrawal(self,WithdrawalMony:int):
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