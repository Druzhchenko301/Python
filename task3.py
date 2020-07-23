n = input("Введите число >>> ")

first_values = "{}{}{}".format(n, n, n)
second_values = "{}{}".format(n, n)

total_values = int(first_values) + int(second_values) + int(n)

print(f"Результат сложения: {first_values} + {second_values} + {n} = {total_values}")
