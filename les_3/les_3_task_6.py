""" Vasilii Sitdikov
GeekBrains Courses. Algorithms
Lesson 3 task 6
October 2019

task: 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
      Сами минимальный и максимальный элементы в сумму не включать.

Решаем задачу за один проход!
Такое решение позволяет обрабатывать данные с ввода "на лету" либо работать с большим объемом данных через стэк
или чанки.
Решение основано на том, что при движении по массиву мы либо нвходимся в тренде
(то есть обновляем глобальный максимум или минимум), либо во флэте (не обновляем глобальные экстремумы).
Для отсутствия дублирования кода используется информация о направлении глобального тренда direction. Фактически
она позволяет писать код только для восходящего тренда, инвертируя его для нисходящего.
"""

# Solution:
# Создание массива
import random
matrix = [random.randint(-100, 100) for _ in range(int(input('Задайте размер списка: ')))]

print(f'Создан список: \n{matrix}')

glob_min = matrix[0]  # Мы всегда будем "обзывать" минимумом первый элемент, а максимумом второй в первом патерне...
glob_max = matrix[1]  # ...  Реальность или инверсность зависит от direction
direction = 1 if matrix[1] > matrix[0] else -1  # Показывает направление глобального тренда
# При direction = -1 glob_max и glob_min меняются местами, также переворачиваются выражения для сравнения
trend = True
sum_trend = sum_flat = turn_point = 0

# Всю задачу решаем за один проход, не создавая массивов
for i in range(2, len(matrix)):

    # Работа в тренде (находимся выше глобального 'максимума' или ниже глобального 'минимума')
    if trend:
        if (matrix[i] - glob_max) * direction > 0:
            sum_trend += matrix[i - 1]
            glob_max = matrix[i]
        # Если проскочили 'вниз' глобальный 'минимум'
        elif (matrix[i] - glob_min) * direction < 0:
            trend = True
            direction *= -1  # Меняем направление тренда и инверсируем 'максимумы' и 'минимумы'
            glob_min = glob_max
            glob_max = matrix[i]
            sum_trend = 0
            continue
        else:
            turn_point = matrix[i - 1]  # Необходимо запомнить значение точки разворота на случай возврата тренда
            trend = False
            sum_flat = 0
            continue

    # Работа во флэте (болтаемся между глобальным максимумом и глобальным минимумом)
    if not trend:
        if (matrix[i] - glob_max) * direction <= 0 and (matrix[i] - glob_min) * direction >= 0:
            sum_flat += matrix[i - 1]
        # Если проскочили 'вниз' глобальный 'минимум'
        elif (matrix[i] - glob_min) * direction < 0:
            trend = True
            direction *= -1  # Меняем направление тренда и инверсируем максимумы и минимумы
            glob_min = glob_max
            glob_max = matrix[i]
            sum_trend = sum_flat + matrix[i - 1]
            continue
        elif (matrix[i] - glob_max) * direction > 0:  # Если вернулись в старый тренд
            trend = True
            glob_max = matrix[i]
            sum_trend += sum_flat + turn_point + matrix[i - 1]

print(f'Искомая сумма: {sum_trend}')

