#3
"""
vsego_naydeno = 0
k = 1050
for chislo in range(k + 1):
    chislo_naoborot = int(str(chislo)[::-1])
    if chislo + chislo_naoborot == k:
        vsego_naydeno += 1
print(vsego_naydeno)
"""
#1
def f(n):
    if len(n) < 2:
        return n
    if n[0] >= n[1]:
        return f(n[1:])
    if len(n) > 2 and n[1] >= n[2]:
        return [n[0]] + f(n[2:])
    if len(n) > 3 and n[2] >= n[3]:
        return [n[0], n[1]] + f(n[3:])
    return [n[0]] + f(n[1:])

print(f([6, 2, 5, 4, 2, 5, 6]))
#2
"""
with open('input.txt', 'r') as file:
    n = int(file.readline())
    spisok = list(map(int, file.readline()))
massiv = [1] * n
for i in range(n):
    for j in range(i):
        if spisok[j] < spisok[i] and massiv[j] + 1 > massiv[i]:
            massiv[i] = massiv[j] + 1
otvet = max(massiv)
with open('output.txt', 'w') as file:
    file.write(str(otvet))
print(otvet)
"""




