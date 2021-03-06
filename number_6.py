# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

start_value = float(input('Укажите расстояние, которое пробежал спортсмен в первый день в км '))
target_value = float(input('укажите целевое расстояние, которое нужно пробежаьт спортсмену '))
if target_value < start_value:
    print('Ухудшение результата не входит в наши планы!')
else:
    days = 1
    print('# 1-й день: {} км'.format(round(start_value,2)))
    while start_value <= target_value:
        days += 1
        start_value = start_value + start_value/10
        print('# {}-й день: {} км'.format(days, round(start_value,2)))
    print('На {} день спортсмен достиг результата - не менее {} км.'.format(days, target_value))
