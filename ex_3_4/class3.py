class BankAccount:
    def __init__(self, account_number: int, name: str, balance: int):
        self.account_number: int = account_number
        self.name: str = name
        self.balance: int = balance
        self.transaction: int = 0

    def deposit(self, deposit_money: int) -> None:
        self.transaction = 1
        self.balance += deposit_money
        print(f'you have a total of {self.balance} after Deposit')

    def withdrawal(self, withdrawal_money: int) -> None:
        self.transaction = 1
        self.balance -= withdrawal_money
        print(f'you have a total of {self.balance} after Withdrawal Mony')

    def bank_fees(self, corrent_balnace: int) -> float:
        if self.transaction == 1:
            corrent_balnace = self.balance - (self.balance * 0.05)
            return corrent_balnace

    def display(self) -> None:
        print('the total detail of your account is :')
        print(f' owner name : {self.name}')
        print(f' accountNumber: {self.account_number}')
        print(f'balance :  {self.balance}')
        print(f'balance after bank fees transaction : {self.bank_fees(self.balance)}')
        self.transaction = 0
