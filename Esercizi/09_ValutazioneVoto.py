vote = int(input("Inserisci un voto da 0 a 100: "))

if vote < 60:
    print("Fail")
elif vote >= 80:
    print("Excellent")
else:
    print("Pass")