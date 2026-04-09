fruits = ["Fragola", "Banana", "Cocco"]

# for el in list

for fruit in fruits:
    print(fruit) # fruit può essere qualsiasi nome 

for i in range(len(fruits)):
    print(f"Elemento {i+1}: {fruits[i]}")

for i, fruit in enumerate(fruits):
    print(f"Elemento {i+1}: {fruit}")



range(10) # 0 - 10
range(1, 10) # 1 - 10
range(1, 10, 2) # va da 1 a 10 a passi di 2