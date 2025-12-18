#1
"""
count = 0
max_summa = 0
with open('39762.txt', 'r') as file:
    chisla = file.readlines()
    chisla = [int(el) for el in chisla]
for i in range(len(chisla) - 1):
    if (chisla[i] * chisla[i+1]) % 15 == 0 and ((chisla[i] + chisla[i+1]) % 7) == 0:
        count += 1
        if max_summa < (chisla[i] + chisla[i+1]):
            max_summa = (chisla[i] + chisla[i+1])
print(count, max_summa)
"""
#2
"""
with open('68279.txt', 'r') as file:
    chisla = file.readlines()
    chisla = [int(el) for el in chisla]
    max_el = 0
    for el in chisla:
        if str(el)[-3:] == "562":
            if max_el < el:
                max_el = el
    c = 0
    max_sum = 0
    for i in range(len(chisla) - 3):
        l = [chisla[i], chisla[i + 1], chisla[i + 2], chisla[i + 3]]
        l5 = [el for el in l if len(str(el)) == 5]
        lnot5 = [el for el in l if len(str(el)) != 5]
        lcrat3 = [el for el in l if el % 3 == 0]
        lcrat7 = [el for el in l if el % 7 == 0]
        if len(l5) >= 1 and len(lnot5) >= 2:
            if len(lcrat3) < len(lcrat7):
                if sum(l) > max_el and sum(l) < max_el * 2:
                    c += 1
                    if max_sum < sum(l):
                        max_sum = sum(l)
print(c, max_sum)
"""
#3
"""with open('40992.txt', 'r') as file:
    chisla = file.readlines()
    chisla = [int(el) for el in chisla]
nechetnye = [el for el in chisla if el % 2 != 0]
if len(nechetnye) > 0:
    srednee = sum(nechetnye) / len(nechetnye)
else:
    srednee = 0
count = 0
max_sum = 0
for i in range(len(chisla) - 1):
    a = chisla[i]
    b = chisla[i + 1]
    uslovie1 = (a % 5 == 0) or (b % 5 == 0)
    uslovie2 = (a < srednee) or (b < srednee)
    if uslovie1 and uslovie2:
        count += 1
        summa = a + b
        if summa > max_sum:
            max_sum = summa
print(count, max_sum)"""

