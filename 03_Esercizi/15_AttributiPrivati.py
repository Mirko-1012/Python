class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
mio_conto = Account(1000)
mio_conto.deposit(500)
print(mio_conto.get_balance())