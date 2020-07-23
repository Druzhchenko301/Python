revenue = int(input("Введите, пожалуйста, выручку фирмы >>> "))
costs = int(input("Введите, пожалуйста, издержки фирмы >>> "))

if revenue > costs:

    profitability = float((revenue - costs) / revenue)

    print(f"Фирма отработала с положительным финансовым результатом. Рентабельность фирмы: {profitability}")
else:
    print("Фирма отработала с отрицательным финансовым результатом ")

number_employees = int(input("Введите, пожалуйста, численность сотрудников >>> "))

profit_per_person = float((revenue - costs) / number_employees)

print(f"Прибыль на одного сотрудника составляет: {profit_per_person}")
