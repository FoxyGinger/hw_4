# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


from random import randint


def create_random_list(size: int) -> list:
    arr = []
    for _ in range(size):
        arr.append(randint(0, 20))

    return arr


def get_intersection(arr1: list, arr2: list) -> list:
    s1, s2 = set(arr1), set(arr2)

    return sorted(s1 & s2)


n = int(input("Введите кол-во элементов в 1 массиве: "))
m = int(input("Введите кол-во элементов во 2 массиве: "))

arr1, arr2 = create_random_list(n), create_random_list(m)
result = get_intersection(arr1, arr2)

print(f'{arr1} & {arr2} -> {result}')