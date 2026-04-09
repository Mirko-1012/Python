a = 0

while a < 5:
    print(a)
    a += 1
else:
    print("Ciclo finito")

#################################################################

b = 0

while b < 5:
    print(b)
    b += 1
    if b == 3:
        break
else:
    print("Ciclo finito")

#################################################################

c = 0

while c < 11:
    c+=1
    if (c % 2 != 0):
        continue
    print(c)
    
else:
    print("Ciclo finito")

#################################################################

a = 0

flag = False

while not flag:
    a += 1

if a == 0:
    flag = True