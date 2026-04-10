ho_fame = False
non_ho_fame = True
mangio = False

controllo_1 = ho_fame and mangio or non_ho_fame
controllo_2 = ho_fame and (mangio or non_ho_fame)

print(controllo_1)
print(controllo_2)