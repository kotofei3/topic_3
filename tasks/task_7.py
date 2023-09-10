hourly_rate: float = float(input('Введите почасовую ставку: '))

working_hours: int = 22 * 8
salary: float = working_hours * hourly_rate

print("Вы проработали", working_hours, "часов")
print("Ваша зарплата в месяц:", salary, "рублей")
