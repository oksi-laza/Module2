from itertools import combinations as com

list_ = list(com(range(1, 21), r=2))
# print(list_)          # вывела получившиеся уникальные пары

# # второй способ формирования уникальных пар
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# list1_object = com(list1, r=2)
# list1_pair = [i for i in list1_object]
# print(list1_pair)      # вывела получившиеся уникальные пары, те же данные, что и 'list_'

while True:
    number = int(input('Введите число от 3 до 20: '))
    if number < 3 or number > 20:
        print('Вы ввели число вне указанного диапазона.')
    else:
        break

list_pairs_password = []
for i in list_:

    pairs = int(''.join(map(str, i)))  # перевела данные в кортеже в 'str', соединила и удалила пробелы, перевела в'int'
    # print(pairs)                         # вывела посмотреть объединенные пары чисел - норм
    # print(sum(i))                        # вывела посмотреть суммы каждой пары чисел - норм
    if number % sum(i) == 0:
        list_pairs_password.append(pairs)

list_pairs_password = int(''.join(map(str, list_pairs_password)))  # перевела в 'str', удалила пробелы, перевела в 'int'
print(f'Для числа {number} пароль {list_pairs_password}')