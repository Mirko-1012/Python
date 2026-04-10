a = []
for i in range(100):
    a.append(i*3)
print(a)

###################################################

l = [i*3 for i in range(100)] # list_comprehention
print(l)

###################################################

l2 = []
for i in range(20):
    if(i % 2 == 0):
        l2.append(i)
print(l2)

###################################################

l3 = [i for i in range(20) if i % 2 == 0]
print(l3)

l4 = [i * 2 for i in range(11)]
print(l4)

###################################################

s = "Ciao a tutti i 25 caciotti"

s2 = s.split()
print(s2)

lw = [len(i) for i in s2]
print(lw)

cw = [i.capitalize() for i in s2]
print(cw)

ow = ["p" if len(i) % 2 == 0 else "d" for i in s2 if not i.isalpha()]
print(ow)