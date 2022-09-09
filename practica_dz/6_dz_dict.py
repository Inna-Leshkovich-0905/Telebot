# задача 1

cars = {'BMW': ['X6', 'X7', 'Z4'], 'Tesla': ['Model S', 'Model X', 'Model Y']}

for key, value in cars.items():
    print(f'Авто: {key}, модель: {value[0]}')
    print(f'Авто: {key}, модель: {value[-1]}')

    # print(f'Авто: {key}, модель: {value[0]}', f'Авто: {key}, модель: {value[-1]} ')