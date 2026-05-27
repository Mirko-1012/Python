class Account:
    def __init__(self, balance):
        self.__balance = balance # attributo privato

    def deposit(self, amount):
        self.__balance += amount # metodo che modifica l'attributo privato

    def get_balance(self):
        return self.__balance # metodo che restituisce il valore dell'attributo privato
    
mio_conto = Account(1000) # creo un'istanza della classe Account con un saldo iniziale di 1000
mio_conto.deposit(500) # deposito 500, il saldo dovrebbe ora essere 1500
print(mio_conto.get_balance()) # Output: 1500, il metodo get_balance restituisce il saldo aggiornato