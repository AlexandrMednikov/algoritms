""" В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random
arr = [random.randint(0, 100) for i in range(0, 10)]
print('Случайный массив: ' + str(arr))
max_arr = (max(arr))
min_arr = (min(arr))
max_i = arr.index(max_arr)
min_i = arr.index(min_arr)
arr[max_i] = min_arr
arr[min_i] = max_arr
print('Массив после свапа: ' + str(arr))