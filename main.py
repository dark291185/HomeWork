"""
Урок 1
У нас есть список покупок и мы хотим понять
сколько денег нам с собой брать.
У нас есть бумажные купюры: 500, 100, 50
Есть монеты: 10, 5, 1
Нужно вывести сколько каждого типа нам нужно.
"""

'''
int - только целые числа
float - дробные числа
'''

#shop_item_str = input('Введите стоимость покупки: ')
#shop_item = float(shop_item_str)
#print(type(shop_item_str), type(shop_item))
'''
item_number = 10
total_price = 0
while item_number > 0:
    shop_item = float(input('Введите стоимость покупки '))
    total_price += shop_item
    #total_price += float(input('Введите стоимость покупки '))
    item_number -= 1
'''

item_number = 2
total_price = 0

for i in range(item_number):
    total_price += float(input('Введите стоимость покупки '))

rub_500 = total_price // 500
left_money = total_price % 500
print(rub_500, left_money)
#rub_100 = left_money // 100
#left_money = left_money % 100
#print(rub_100, left_money)
rub_20 = left_money // 20
left_money = left_money % 20
print(rub_20, left_money)
