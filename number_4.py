# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

input_number = float(input('Введите целое число '))

if input_number % 1 != 0:
    print('Хулиганишь! Все равно возьму только целую часть!')
    input_number = int(input_number)
else:
    input_number = int(input_number)

counter = 0
max_value = 0

while counter < len(str(input_number)):
    current_value = int(str(input_number)[counter])
    if current_value > max_value:
        max_value = current_value
    counter += 1

print('Наибольшая цифра в числе {}'.format(max_value))