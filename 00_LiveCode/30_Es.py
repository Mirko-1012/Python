try: 
    a = int(input("Inserisci un numero: "))
    b = 5 / a
    print(b)
except (ValueError, ZeroDivisionError) as e: # Si possono gestire più errori in un singolo except
    print(f"Errore di input {e}, {type(e)} Cane!")
    print(f"Errore di input {str(e)}, {repr(e)} Cane!")
except:
    print("Qualcosa è andato storto")

else: # Si attiva quando il try va a buon fine
    print("Andato a buon fine")

finally: # Questo si attiva in ogni caso
    print("Fine Paloma")

##########################################################################################################

try: 
    c = int(input("Inserisci un numero: "))
    d = 5 / c
    print(d)
except ZeroDivisionError as er:
    print("Non puoi dividere per 0. Cane")
    raise ZeroDivisionError("Te l'avevo detto che non potevi dividere per 0. Lampato") # Fa chiudere il programma

##########################################################################################################

age = int(input("Inserisci età utente: "))

if age > 120 or age < 0:
    raise ValueError("Età non verosimile")

##########################################################################################################

class VehicleError(Exception):
    def __init__(self, message = "Vehicle is broken"):
        super().__init__(message)


f = input()

#if Vehicle.doors > 9       # Errore creato da noi
#    raise VehicleError