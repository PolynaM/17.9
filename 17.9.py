n = input("Введите список чисел через пробел: ")
n_list = [int(a) for a in n.split()]
value = int(input('Введите любое число: '))

if (' ' not in (n)):
    raise ValueError('Введите числа через пробел!')

def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
        return array
n_list = qsort(n_list, 0, len(n_list)-1)

def binary_search(array, value, left, right):
    try:
        if left > right:
            return False
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif value < array[mid]:
            return binary_search(array, value, left, mid-1)
        else:
            return binary_search(array, value, mid+1, right)
    except IndexError:
        return 'Число выходит за диапазон списка'

print('Сортированный список: ', n_list)

if not binary_search(n_list, value, 0, len(n_list)):
    rI = min(n_list, key=lambda x: ((x - value, x)))
    ind = n_list.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < value:
        print(f'''В списке нет введенного числа 
Ближайшее меньшее число: {rI}, индекс: {ind}
Ближайшее большее число: {n_list[max_ind]} индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного числа 
Ближайшее меньшее число: {rI}, его индекс: {n_list.index(rI)}
В списке нет меньшего элемента''')
    elif rI > value:
        print(f'''В списке нет введенного числа
Ближайшее большее число: {rI}, его индекс: {n_list.index(rI)}
Ближайшее меньшее число: {n_list[min_ind]} его индекс: {min_ind}''')
    elif n_list.index(rI) == 0:
        print(f'Индекс введенного числа: {n_list.index(rI)}')
else:
    print(f'Индекс введенного числа: {binary_search(n_list, value, 0, len(n_list))}')