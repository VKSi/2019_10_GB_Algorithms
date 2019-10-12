# Vasilii Sitdikov
# GeekBrains Courses. Algorithms
# Lesson 3 task 5
# October 2019

# task: 5. В массиве найти максимальный отрицательный элемент.
#       Вывести на экран его значение и позицию в массиве.

# Solution:
# Создание массива
import random
matrix = [random.randint(-100, 100) for _ in range(int(input('Задайте размер списка: ')))]
print(f'Создан список: \n{matrix}')

# Мы не можем воспользоваться нулем для сравнения, первый отрицательный элемент будем считать наибольшим
no_negative = True    # Нужно отслеживать, были ли вообще отрицательные числа
for i in range(len(matrix)):
    if matrix[i] < 0:
        if no_negative:
            a = matrix[i]
            pos = i
            no_negative = False
        elif matrix[i] > a:
            a = matrix[i]
            pos = i
if no_negative:
    print("В заданном массиве нет отрицательных чисел")
else:
    print(f'Максимальный отрицательный элемент массива находится на позиции {pos + 1} со значением {a}')
