#1
# присваиваем переменным значения
name = 'Diana'
email = '22005'
# выводим значения на экран
print('My name:', name)
print('My e-mail:', email)

2
# просим пользователя ввести длину и ширину в футах
len_fut = int(input('Введите длину участка в футах: '))
width_fut = int(input('Введите ширину участка в футах: '))

# выводим площадь в акрах
print('Площадь участка в акрах равна:', ((len_fut * width_fut) / 43560))

#3
# просим пользователя ввести сумму заказа в ресторане
rest_bill = int(input('Введите сумму заказа в ресторане: '))
# высчитываем сумму налога и чаевых
tax_sum = rest_bill * 0.13
tip_sum = rest_bill * 0.18

# выводим результат программы
print('Сумма налога:', round(tax_sum, 3))
print('Сумма чаевых:', round(tip_sum, 3))
print('Итоговая сумма:', round((rest_bill + tip_sum + tax_sum), 2))

#4
# импортируем модуль math
import math

# просим пользователя ввести длину и количсетво сторон
side = int(input('Введите длину стороны: '))
side_amount = int(input('Введите количество сторон: '))

# рассчитываем площадь заданного многоугольника
area = (side_amount * side ** 2) / (4 * math.tan(math.pi/side_amount))

# выводим результат
print(area)

#5
# просим пользователя ввести возраст посетителей
visitor_age = int(input('Введите возраст посетителя: '))
cost = 0

# пока возраст посетителя не равен пустой строке запускаем цикл
while visitor_age != '':
    if 3 < int(visitor_age) < 13:
        cost += 14.00
    elif 13 < int(visitor_age) < 66:
        cost += 23.00
    elif int(visitor_age) > 66:
        cost += 18.00
    else:
        cost += 0.00
    visitor_age = input('Введите возраст посетителя: ')

# выводим общую стоимость билетов
print(f'Общая стоимость билетов: {round(cost, 2)} $')