'''
случай с ограничением на трату (не больше 420 рублей)
'''
left_money = 420
total_price = 0
while total_price <= 420:
    shop_item = float(input('Введите стоимость покупки '))
    if (left_money - shop_item) > 0:
        #print('Block 1')
        # print('total_price, left_money')
        total_price += shop_item
        left_money = 420 - total_price
        #left_money -= shop_item
    elif (left_money - shop_item) == 0:
        #print('Block 2')
        # print('total_price, left_money')
        total_price += shop_item
        left_money = 420 - total_price
        break
        # print('total_price, left_money')
    else:
        print('Недостаточно денег ')
    print('Сколько денег осталось: ', left_money)
    # total_price += float(input('Введите стоимость покупки '))
print(total_price)