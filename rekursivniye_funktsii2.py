#1
"""
def task1(tekushee, konec):
    if tekushee > konec:
        return 0
    if tekushee == konec:
        return 1
    return task1(tekushee + 1, konec) + task1(tekushee + 2, konec) + task1(tekushee * 2, konec)

print(task1(3, 10) * task1(10, 12))
"""
#2
"""
def task2(tekushee):
    if tekushee == 26:
        return 0
    if tekushee > 27:
        return 0
    if tekushee == 27:
        return 1

    return task2(tekushee + 1) + task2(2 * tekushee + 1)

print(task2(1))
"""
#3
"""
def task3(tekushee, konec, zapret=[]):
    if tekushee > konec:
        return 0
    if tekushee == konec:
        return 1
    if tekushee in zapret:
        return 0
    return (task3(tekushee + 1, konec, zapret) + task3(tekushee + 2, konec, zapret))

a = task3(2, 9)
b = task3(9, 18, [14])
print(a * b)
"""