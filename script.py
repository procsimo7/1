price_all = 0

n = int(input('Введите колличество билетов'))

for i in range(n):
    i += 1
    while True:
        try:
            a = int(input(f'Для какого возраста билет №{i}? '))
            if a < 18:
                print('Билет бесплатный')
            elif 25 > a >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(a) == int:
                break
        except ValueError:
            print('Введите целое число')
if n > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-x человек')
else:
    print(f'Сумма к оплате {price_all} руб.')