# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


import random,math
numbers = [random.randint(0, 10) for _ in range(int(input('Введите количество элементов списка: ')))]

print(f'Начальный список -> {numbers}')
multiplication_list = list(map(lambda i: (numbers[i]*numbers[-(i+1)]), [i for i in range(math.ceil(len(numbers)/2))]))
print(f'Произведение пар элементов списка -> {multiplication_list}')