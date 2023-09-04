name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = int(input('Введите ваш возраст: '))

# вывод типа и идентификатора каждой переменной
print("Тип имени:", type(name), "ID в памяти:", id(name))
print("Тип фамилии:", type(surname), "ID в памяти:", id(surname))
print("Тип возраста:", type(age), "ID в памяти:", id(age))
