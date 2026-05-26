number = [1, 2, 3, 4, 5, 10, 50, 60, 70, 80, 90, 100]

filtered = list(filter(lambda x : x > 10, number))
print(filtered)

 # filter() è una funzione built-in di Python che consente di filtrare gli elementi di un iterabile (come una lista)
 # in base a una condizione specificata da una funzione. 
 # In questo caso, stiamo usando una funzione lambda per filtrare i numeri maggiori di 10 dalla lista "number". 
 # Il risultato è convertito in una lista utilizzando la funzione list()).