from abc import ABC, abstractmethod
class Payment(ABC):
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, number_card, cardholder_name, balance):
        self.number_card = number_card
        self.cardholder_name = cardholder_name
        self.balance = balance
    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Thẻ {self.number_card} của {self.cardholder_name} đã trả số tiền {amount}')
        else:
            print('Số dư tài khoản không đủ')

class PayPalPayment(ABC):
    def __init__(self, account_paypal, balance):
        self.account_paypal = account_paypal
        self.balance = balance
    def pay(self, amount):
        if amount <= self.balance:
            print(f'Tài khoản Paypal {self.account_paypal} đã trả số tiền {amount}')
        else:
            print('Số dư không đủ')

credit = CreditCardPayment(12345, 'jame', 13000)
credit.pay(1000)
paypal = PayPalPayment('ghty', 3000)
paypal.pay(4500)
cre_pal = [credit, paypal]
for obj in cre_pal:
    obj.pay(2000)