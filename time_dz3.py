time_1h = float(input('Введите количество времени, которое потратили на первое задание, часов: '))
time_1m = float(input('Введите количество времени, которое потратили на первое задание, минут: '))
time_1mh = float(time_1h*60 + time_1m)
time_2mh = float(time_1mh / 2)
hours, minutes = divmod(time_2mh, 60)
print = ('На второе задание вы потратили: ',"%02d:%02d"%(hours,minutes))
#time_3mh = time_2mh/2
#hours, minutes = divmod(time_3mh, 60)
#print = ('На третье задание вы потратили: ', "%02d:%02d"%(hours, minutes))
#time_dz_all = time_1mh+time_2mh+time_3mh
#hours, minutes = divmod(time_dzall, 60)
#print = ('Всего на дз вы потратили: ', "%02d:%02d"%(hours,minutes))