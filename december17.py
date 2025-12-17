#1
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 < 1 or x1 > 8 or y1 < 1 or y1 > 8 or x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8:
    print("Ошибка!")
else:
    raznitsaX = abs(x1 - x2)
    raznitsaY = abs(y1 - y2)
    if (raznitsaX == 2 and raznitsaY == 1) or (raznitsaX == 1 and raznitsaY == 2):
        print("Может")
    else:
        print("Не может")
"""
#3
"""
vsego = 0
while True:
    num = int(input())
    if num == 0:
        break
    vsego += num
print(vsego)
"""
#4
"""
chisloN = int(input("N:"))
factorial = 1
for i in range(1, chisloN + 1):
    factorial = factorial * i
print(factorial)
"""
#2
"""
chisloK = int(input("K:"))
chisloN = int(input("N:"))
sum = 0
for i in range(chisloK, chisloN + 1):
    if i % 2 == 0:
        sum += i
print(sum)
"""




