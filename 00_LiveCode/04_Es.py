s = "Hello World"

print(s.capitalize()) # Prima lettera maiuscola
print(s.upper()) # Rende tutto maiuscolo
print(s.lower()) # Rende tutto minuscolo

s2 = "   Paloma   "

print(s2)
print(s2.strip()) # Rimuove gli spazi all'inizio e alla fine
print(s2.replace("Paloma","Paurina")) # Rimpiazza la prima parola con la seconda

print(s2)

s3 = " hello woRLd"

print(s3.lower().strip().capitalize())

s4 = "123abc"
s5 = "123abc-?"
s6 = "123"
s7 = "CIAO"

print(s4.isalnum(), s5.isalnum()) # Restituisce true o false se il valore è alfanumerico o no
print(s4.isdigit(), s6.isdigit()) # Restituisce true o false se il valore e numerico o no
print(s7.isupper()) # Restituisce true o false se il valore è tutto maiuscolo o no