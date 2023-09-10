name: str = input('Введите ваше имя: ')
surname: str = input('Введите вашу фамилию: ')
age: int = int(input('Введите ваш возраст: '))

# вывод типа и идентификатора каждой переменной
print("Тип имени:", str(type(name)) + ",", "ID в памяти:", id(name))
print("Тип фамилии:", str(type(surname)) + ",", "ID в памяти:", id(surname))
print("Тип возраста:", str(type(age)) + ",", "ID в памяти:", id(age))
