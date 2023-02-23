price = 0
number_of_tickets = int(input('Введите количество билетов: '))
for i in range(number_of_tickets):
    i += 1
    age = int(input(f'Введите возраст посетителя по {i} билету: '))
    if age < 18:
            print('Цена билета - 0 руб.')
    elif 18 <= age < 25:
            price += 990
            print('Цена билета - 990 руб.')
    else:
            price += 1390
            print('Цена билета - 1390 руб.')
if number_of_tickets > 3:
    all_price = (price) * 0.9
    print(f'Сумма к оплате - {all_price} руб., учитывая скидку 10% (больше трёх человек)')
else:
    print(f'Сумма к оплате - {price} руб.')