#27686
"""
max_dlina = 0
tekushaya_dlina = 0
with open("27686.txt", "r") as file:
    stroka = file.read()
for simvol in stroka:
    if simvol == 'X':
        tekushaya_dlina += 1
        if tekushaya_dlina > max_dlina:
            max_dlina = tekushaya_dlina
    else:
        tekushaya_dlina = 0
print(max_dlina)
"""
#36037
max_dlina = 0
tekushaya_dlina = 0
with open('36037.txt') as file:
    stroka = file.read()
for i in range(len(stroka)):
    if stroka[i:i+4] == "XZZY":
        if tekushaya_dlina > max_dlina:
            max_dlina = tekushaya_dlina
        tekushaya_dlina = 0
    else:
        tekushaya_dlina += 1
if tekushaya_dlina > max_dlina:
    max_dlina = tekushaya_dlina
print(max_dlina)
#46982
"""
count = 0
index = 0
with open("46982.txt") as file:
    text = file.read()
while index < len(text):
    if text[index] == 'E':
        end = index + 1
        while end < len(text) and text[end] not in 'EF': 
            end += 1
        if end < len(text) and text[end] == 'E' and end - index + 1 >= 12: 
            count += 1 
            index = end
        else: 
            index += 1
    else: 
        index += 1
print(count)
"""
