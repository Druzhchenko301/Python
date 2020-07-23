positive_integer = int(input("Введите, пожалуйста, целое пложительное число >>> "))
max_positive_integer = positive_integer % 10
positive_integer = positive_integer // 10
while positive_integer > 0:
    if positive_integer % 10 > max_positive_integer:
        max_positive_integer = positive_integer % 10
    positive_integer = positive_integer // 10
print(f"Самая большая цифра в числе {max_positive_integer}")
