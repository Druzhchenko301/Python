result_first_day = float(input("Введите результат спортсмена в первый день >>> "))
max_result = float(input("Введите результат спортсмена, оторый он должен достичь >>> "))

number_day = 1
print("Результат:")
print("{}-й день: {:.2f}".format(number_day, result_first_day))

while True :
    if result_first_day >= max_result :
        print("{}-й день: {:.2f}".format(number_day, result_first_day))
        print("Ответ: на {}-й день спортсмен достиг результата — не менее {} км".format(number_day, max_result))
        break
    result_first_day = float(result_first_day + (result_first_day * 0.1))
    number_day += 1

    if result_first_day <= max_result :
        print("{}-й день: {:.2f}".format(number_day, result_first_day))
        continue
