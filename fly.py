from geopy.distance import geodesic as GD 

speed = float(input('Введите скорость самолета: '))
track_a= input('Введите город вылета: ' )
track_b= input('Введите город прилета: ' )
distance = float(input('Введите расстояние между городом вылета и городом прилета: '))
time = distance/speed
print('От ', track_a, 'до ', track_b, 'лететь ', time, 'часов')                 