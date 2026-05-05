class Account:
    def __init__(self, balance):
        self.__balance = balance

    def __log_transaction(self, message):
        print(f"{message}")

    def deposit(self, amount):
        self.__balance += amount
        self.__log_transaction(f"Versamento di {amount} effettuato con successo.")

    def get_balance(self):
        return self.__balance
    
mio_conto = Account(1000)
mio_conto.deposit(500)