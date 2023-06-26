# coding: utf-8
# Посчитать возраст по году, месяцу и дню рождения
current_year = 2023
current_month = 6
current_date = 26
your_year = int(input('Your year of birth: '))
your_month = int(input('Your month of birth: '))
your_date = int(input('Your date of birth: '))
# input в качестве параметра принимает подскаку к вводу


print(your_year)
print(type(your_year))
#print(current_year - your_year)

# Явное преобразование типа
your_year = int(your_year)
my_age = current_year - your_year
if your_month > current_month:
    print(my_age-1)
elif your_month==current_month and your_date <= current_date:
    print(my_age)
if my_age > 18:
    print('Взрослый')
#  print('Совсем большой')
print('Совсем большой')
               
print(9)

# Отступы: правее - вход в управляющую
# конструкцию: цикл, ветвление, функцию, класс
#          левее - выход (оканчание) блока


# Отступ 4 пробела
# unindent - уменьшение количества отступов
# indentation error - ошибка отступов
# python enhancement proposals
# PEP8 - красивый, удобный, аккуратный код

# Практика и дз:
# https://docs.google.com/presentation/d/1AHgij7KgVNdm5V3ptXqXj4aE-ula_btRos19V68BoU8/edit#slide=id.g108bed2ac70_0_0

# С помощью if проверить, что из перечисленного
# является истинным, а что - ложным?
# 3, 0, '', [], False, True, 'mama'
if 7:
    print(7, 'истинно')

# ДЗ: дописать задачку про возраст,
# запросив день и месяц рождения
# ПАНДА-ПАРК: есть 4 трассы
# чёрная, красная, зеленая, синяя
# от 170 см, 155, 140 и остальные

# Обе задачки на python, html+js


