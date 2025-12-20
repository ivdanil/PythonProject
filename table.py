import csv
"""
with open("36031.csv", "r") as file:
    n = list(csv.reader(file))
    l = []
    for i in range(len(n)):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
l = l[::-1]
l = [row[::-1] for row in l]
stroki = len(l)
stolbtsi = len(l[0])
summa = [[0] * stolbtsi for i in range(stroki)]
otkuda = [[""] * stolbtsi for i in range(stroki)]
summa[0][0] = l[0][0]
for j in range(1, stolbtsi):
    summa[0][j] = summa[0][j-1] + l[0][j]
    otkuda[0][j] = 'L'
for i in range(1, stroki):
    summa[i][0] = summa[i-1][0] + l[i][0]
    otkuda[i][0] = 'U'
for i in range(1, stroki):
    for j in range(1, stolbtsi):
        if summa[i-1][j] > summa[i][j-1]:
            summa[i][j] = summa[i-1][j] + l[i][j]
            otkuda[i][j] = 'U'
        else:
            summa[i][j] = summa[i][j-1] + l[i][j]
            otkuda[i][j] = 'L'
print(summa[-1][-1])
p = []
a = stroki-1
b = stolbtsi-1
while a != 0 or b != 0:
    if otkuda[a][b] == 'U':
        p.append("вверх")
        a -= 1
    else:
        p.append("влево")
        b -= 1
p.reverse()
for i in range(len(p)):
    print(p[i], end=" ")
"""
#1
"""
otvet = 0
with open("59778.csv", "r") as f:
    for line in f:
        nums = list(map(int, line.strip().split(';')))
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        values = list(count.values())
        if 4 not in values:
            continue
        rep = []
        uniq = []
        for n, cnt in count.items():
            if cnt == 4:
                rep.append(n)
            else:
                uniq.append(n)
        sum_rep = rep[0] * 4
        avg_uniq = sum(uniq) / 3
        if avg_uniq > sum_rep:
            otvet += 1
print(otvet)
"""
#1
"""
count = 0
with open("59778.csv", "r") as file:
    file = list(csv.reader(file))
l = []
for i in range(len(file)):
    a = (file[i][0].split(";"))
    a = [int(el) for el in a]
    l.append(a)
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i].count(l[i][j]) == 4:
            repeat = l[i][j]
            x = []
            for j in range(len(l[i])):
                if l[i][j] not in x and l[i][j] != repeat:
                    x.append(l[i][j])
            summa_repeat = 4*repeat
            average_sum = sum(x) / len(x)
            if average_sum > summa_repeat:
                count +=1
print(count//4)
"""
#2
max_sum = 0
current_sum = 0
chisla = []
with open('29666.csv', 'r') as f:
    for line in f:
        value = line.strip().replace(',', '.')
        if value:
            chisla.append(float(value))
n = len(chisla)
for i in range(1, n):
    if chisla[i] < chisla[i - 1]:
        current_sum += chisla[i]
    else:
        current_sum = chisla[i]
    if current_sum > max_sum:
        max_sum = current_sum
for num in chisla:
    if num > max_sum:
        max_sum = num
print(max_sum)

