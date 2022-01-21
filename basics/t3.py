print("введите вашу зарплату")
salary = input()
print(f"введено {salary=}")
print("пробуем преобразовать строку в число")
salary = int(salary)
print(f"преобразованное число {salary=}" )
yearly_salary = 12 * salary
print("ваша годовая зарплата")
print(yearly_salary)

# 1 позьзователь вводит свою месячную зп
# 2 пользователь вводит свои месячные затраты
# 3 программ вычисляет баланс доходов и расходов за год на основании двух введеных пользователем чисел
# 4 программа выводит итоговый годовой баланс на экран и если баланс соствляет меньше одной месячной зп - Лох

print("введите ваши месячные затраты")
expenses = input()
expenses = int(expenses)
yearly_expenses = 12 * expenses
print(f"расходы за год {yearly_expenses=}")
balance = yearly_salary - yearly_expenses
print(f"ваш баланс за год {balance=}")

if salary > balance:
    print("Ваши затраты слишком велики, зарабатывайте больше, либо учитесь экономить")
