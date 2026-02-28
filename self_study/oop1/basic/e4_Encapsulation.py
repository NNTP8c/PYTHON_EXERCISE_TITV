class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Đã nạp {amount}. Số dư hiện tại: {self.__balance}')
        else:
            print('Số tiền nạp phải lớn hơn 0.')
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f'Đã rút {amount}. Số dư hiện tại: {self.__balance}')
        else:
            print('Số tiền rút phải lớn hơn 0 và không được vượt quá số dư hiện tại.')

account = BankAccount(10000)
account.deposit(5000)
account.withdraw(3000)
account.withdraw(15000)
print(account.__balance)
        