# В целом все  правильно
# только тип получаемого значения должен быть дробным числом, а не целым
hourly_rate = int(input('Введите почасовую ставку: '))

working_hours = 22 * 8

salary = working_hours * hourly_rate

print("Вы проработали", working_hours, "часов")
print("Ваша зарплата в месяц:", salary, "рублей")
