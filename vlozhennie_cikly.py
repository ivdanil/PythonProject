#1
"""
osnovanie = 15
stroka = "0123456789ABCDE"
otvet_15 = ""
naideno = False
for x in range(15):
    if not naideno:
        chislo1 = int("123" + str(x) + "5", osnovanie)
        chislo2 = int("1" + str(x) + "233", osnovanie)
        summa = chislo1 + chislo2
        if summa % 14 == 0:
            chastnoe = summa // 14
            print(chastnoe)
            temp = chastnoe
            if temp == 0:
                otvet_15 = "0"
            else:
                while temp > 0:
                    otvet_15 = stroka[temp % osnovanie] + otvet_15
                    temp //= osnovanie
                print(otvet_15)
                naideno = True
"""
#2
"""
chislo1 = "F024A89"
chislo2 = "AB267D1"
tsifry = "0123456789ABCDEF"
summa1 = 0
for simvol in chislo1:
    for j in range(len(tsifry)):
        if tsifry[j] == simvol:
            summa1 += j
summa2 = 0
for simvol in chislo2:
    for j in range(len(tsifry)):
        if tsifry[j] == simvol:
            summa2 += j
osnovanie = 16
otvet = 0
obschaya_summa = summa1 + summa2
while osnovanie < obschaya_summa + 1:
    if obschaya_summa % (osnovanie - 1) == 0 and otvet == 0:
        pervoechislo = 0
        for simvol in chislo1:
            for j in range(len(tsifry)):
                if tsifry[j] == simvol:
                    pervoechislo = pervoechislo * osnovanie + j
        vtorochislo = 0
        for simvol in chislo2:
            for j in range(len(tsifry)):
                if tsifry[j] == simvol:
                    vtorochislo = vtorochislo * osnovanie + j
        if (pervoechislo + vtorochislo) % (osnovanie - 1) == 0:
            otvet = osnovanie
    osnovanie += 1
print(otvet)
"""
#3
"""
minimum = 999999
for x in range(10):
    chislo1 = int(str(x) + 'B09', 17)
    chislo2 = int(str(x) + '8E8', 15)
    summa = chislo1 + chislo2
    if not summa % 155:
        chastnoe = summa // 155
        if chastnoe < minimum:
            minimum = chastnoe
print(minimum)
"""
#4
"""
minimum = 999999
otvet = 0
for x in range(11):
    for y in range(8):
        if x >= 8:
            continue
        pervoechislo = int(str(y) + "0" + "4" + str(x) + "5", 11)
        vtorochislo = int("253" + str(x) + str(y), 8)
        summa = pervoechislo + vtorochislo
        if summa % 117 == 0:
            chastnoe = summa // 117
            if summa < minimum:
                minimum = summa
                otvet = chastnoe
print(otvet)
"""
#5
kolvo = 0
virazhenie = 7 * 512**1912 + 6 * 64**1954 - 5 * 8**1991 - 4 * 8**1980 - 2022
while virazhenie != 0:
    ostatok = virazhenie - (virazhenie // 8) * 8
    if ostatok == 7:
        kolvo = kolvo + 1
    virazhenie = virazhenie // 8

print(kolvo)



