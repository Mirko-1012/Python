numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadratiPari = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeri))) # Utilizza filter per selezionare i numeri pari e map per calcolare i quadrati

print(f"Quadrati dei numeri pari: {quadratiPari}")

