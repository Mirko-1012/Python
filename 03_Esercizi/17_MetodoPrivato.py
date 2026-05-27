class Account:
    def __init__(self, balance):
        self.__balance = balance

    def __log_transaction(self, message): # Metodo privato per registrare le transazioni
        print(f"{message}")

    def deposit(self, amount):
        self.__balance += amount # Aggiorna il saldo e chiama il metodo privato per registrare la transazione
        self.__log_transaction(f"Versamento di {amount} effettuato con successo.")

    def get_balance(self): # Metodo pubblico per ottenere il saldo, che utilizza il metodo privato per registrare l'accesso al saldo
        return self.__balance
    
mio_conto = Account(1000) # Creazione di un account con un saldo iniziale di 1000
mio_conto.deposit(500) # Effettua un deposito di 500, che aggiorna il saldo e registra la transazione tramite il metodo privato __log_transaction