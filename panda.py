# ПАНДА-ПАРК: есть 4 трассы
# чёрная, красная, зеленая, синяя
# от 170 см, 155, 140 и остальные


your_height = int(input('Your height: '))
if your_height >= 170:
    print('Ваша трасса - черная ', your_height, '- рост равен или больше 170см')
elif your_height >= 155 and your_height < 170:
    print('Ваша трасса - красная ', your_height, ' - рост в диапазоне от 155см до 170см')
elif your_height >= 140 and your_height < 155:
    print('Ваша трасса - зеленая ', your_height, ' - рост в диапазоне от 140см до 155см')
elif your_height < 140:
    print('Ваша трасса - синяя ', your_height, '- рост меньше 140см')