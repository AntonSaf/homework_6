# Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.

# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]


import random

from random import randint

new_list = [randint(1, 100) for i in range(200)]  
numbers = list(filter(lambda x: x[0] != x[1], enumerate(new_list)))
print(numbers)