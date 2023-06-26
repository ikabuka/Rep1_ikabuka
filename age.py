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
elif my_age < 18:
    print('Подрастающее поколение')
