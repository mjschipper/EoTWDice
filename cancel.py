dct = {0: [4, 2, 3, 2], 1: [2, 3, 6]}
new_dct = dct[0].copy()
for i in new_dct:
    if i in dct[1]:
        dct[0].remove(i)
        dct[1].remove(i)
print(dct)