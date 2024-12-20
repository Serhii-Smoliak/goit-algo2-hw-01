# Завдання 2. Пошук k-го найменшого елемента

import random

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)  # Вибір опорного елемента
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    if k <= len(less):
        return quick_select(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        return quick_select(greater, k - len(less) - len(equal))

# Приклад використання
# arr = [3, 2, 1, 5, 4, 6, 7]
# k = 3
# print(quick_select(arr, k))  # Виведе 3 (3-й найменший елемент)
