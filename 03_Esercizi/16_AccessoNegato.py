class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
mio_conto = Account(1000)
mio_conto.deposit(500)

#print(f"Saldo via name Mangling: {mio_conto._Account__balance}") # Name mangling funzionante, se togliamo il commento darà errore
