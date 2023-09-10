line: str = input('Введите строку: ')
num: int = int(input('Введите число: '))

result: str = '\n'
print((line + result) * num, end='')

# -------------------- Про end и sep

# print(10, end=' ')
# print(20, end=' ')
# print(30, end='')

# print(40, 50, 60, sep='$', end='')
