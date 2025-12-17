# 1
"""
def fibonacci(n):
    l = [0, 1]
    for i in range(n-2):
        new = l[0] + l[1]
        l = [l[1], new]
    return l[1]
n = int(input())
print(fibonacci(n))
"""
#2
"""
chisloN = int(input())
massiv = [0] * (chisloN + 1)
massiv[1] = 1
for i in range(2, chisloN + 1):
    massiv[i] = massiv[i - 1]
    if i > 2:
        massiv[i] += massiv[i - 2]
    if i > 3:
        massiv[i] += massiv[i - 3]
print(massiv[chisloN])
"""
#3
coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1]
]

stroki = len(coins)
stolbtsi = len(coins[0])
summa_monetok = [[0] * stolbtsi for i in range(stroki)]
otkuda = [[''] * stolbtsi for i in range(stroki)]
summa_monetok[0][0] = coins[0][0]
for j in range(1, stolbtsi):
    summa_monetok[0][j] = summa_monetok[0][j - 1] + coins[0][j]
    otkuda[0][j] = 'L'
for i in range(1, stroki):
    summa_monetok[i][0] = summa_monetok[i - 1][0] + coins[i][0]
    otkuda[i][0] = 'U'
for i in range(1, stroki):
    for j in range(1, stolbtsi):
        if summa_monetok[i - 1][j] > summa_monetok[i][j - 1]:
            summa_monetok[i][j] = summa_monetok[i - 1][j] + coins[i][j]
            otkuda[i][j] = 'U'
        else:
            summa_monetok[i][j] = summa_monetok[i][j - 1] + coins[i][j]
            otkuda[i][j] = 'L'
print(summa_monetok[-1][-1])
put = []
x, y = stroki - 1, stolbtsi - 1
while x or y:
    if otkuda[x][y] == 'U':
        put.append("вниз")
        x -= 1
    else:
        put.append("вправо")
        y -= 1
put.reverse()
for i in range(len(put)):
    print(put[i],end=" ")



