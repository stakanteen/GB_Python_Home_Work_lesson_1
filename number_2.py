# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_s_inp = int(input('insert time in seconds '))

time_h = time_s_inp//3600
if time_h < 10:
    time_h_print = str('0') + str(time_h)

time_m = (time_s_inp-time_h*3600)//60
if time_m < 10:
    time_m_print = str('0') + str(time_m)

time_s_calc = time_s_inp - time_h*3600 - time_m*60
if time_s_calc < 10:
    time_s_print = str('0') + str(time_s_calc)

print('{}:{}:{}'.format(time_h_print, time_m_print, time_s_print))
