import os
import sys

# Добавляем путь к библиотеке
sys.path.insert(0, '/app/geometric_lib')

import circle
import square

# Читаем данные из переменных окружения
shape = os.environ.get('SHAPE', 'circle')
size1 = float(os.environ.get('SIZE1', '5'))
size2 = float(os.environ.get('SIZE2', '3'))

print(f"=== Geometric Library Calculator ===")
print(f"Фигура: {shape}")

if shape == 'circle':
    print(f"Радиус: {size1}")
    print(f"Площадь круга: {circle.area(size1)}")
    print(f"Периметр круга: {circle.perimeter(size1)}")

elif shape == 'square':
    print(f"Сторона: {size1}")
    print(f"Площадь квадрата: {square.area(size1)}")
    print(f"Периметр квадрата: {square.perimeter(size1)}")

else:
    print(f"Неизвестная фигура: {shape}")
