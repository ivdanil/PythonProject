#1
"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
"""
#2
"""
def remove_vowels(string):
   vowels = ['e', 'u', 'y', 'o', 'i', 'a']
   if string == "":
       return ""
   if string[0] in vowels:
       return remove_vowels(string[1:])
   else:
       return string[0] + remove_vowels(string[1:])

print(remove_vowels("apple"))
"""
#3
"""
def pascal(n):
    if n == 1:
        return [1]
    pred = pascal(n - 1)
    row = [1]
    for i in range(len(pred) - 1):
        row.append(pred[i] + pred[i + 1])
    row.append(1)
    return row

print(pascal(1))
print(pascal(2))
print(pascal(3))
"""
#final boss
"""
def solve(maze):
    rows = len(maze)
    cols = len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 's':
                start_r = r
                start_c = c
    visited = set()
    def vGlubinu(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return None
        if maze[r][c] == '#' or (r, c) in visited:
            return None
        if maze[r][c] == 'x':
            return []
        visited.add((r, c))
        result = vGlubinu(r - 1, c)
        if result is not None:
            return ['up'] + result
        result = vGlubinu(r + 1, c)
        if result is not None:
            return ['down'] + result
        result = vGlubinu(r, c - 1)
        if result is not None:
            return ['left'] + result
        result = vGlubinu(r, c + 1)
        if result is not None:
            return ['right'] + result
        return None
    return vGlubinu(start_r, start_c)

maze = [
    's----',
    '##---',
    '---##',
    '----x'
]
otvet = solve(maze)
print(otvet)
"""






