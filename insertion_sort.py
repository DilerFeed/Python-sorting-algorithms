import random
import time

def main():
    # Заповнюємо масив для сортування
    type = 1
    N = int(input("Введіть кількість елементів масиву: "))
    array = []
    # Випадково
    if type == 1:
        for i in range(N):
            array.append(random.randint(0,100))
    # Відсортований
    elif type == 2:
        for i in range(N):
            array.append(int(i))
    # Відсортований у зворотньому порядку
    elif type == 3:
        for i in range(N):
            array.append(int(i))
        array = array[::-1]

    
    print("-----------------")
    print("Початковий масив:")
    print(array)

    # Сортування вставками
    # Для кожного елементу масиву
    ref_time = time.perf_counter()
    for i in range(len(array)):
        j = i - 1
        # Вибираємо елемент (ключ)
        key = array[i]
        # Поки зліва елемент більше поточного і він існує
        while array[j] > key and j >= 0:
            # Переставляємо цей елемент праворуч і переходимо на 1 клітинку лівіше
            array[j + 1] = array[j]
            j -= 1
        # Ставимо праворуч від меншого елемента вибраний (ключ)
        array[j + 1] = key
        """
        # Вивести дані по часу сортування по 10 елементів
        cur_time = time.perf_counter()
        if (i + 1) % 10 == 0:
            print(f"Відсортовано {i + 1} елементів за {cur_time - ref_time} секунд!")
        """

    # Вивести дані по часу сортування всіх елементів
    cur_time = time.perf_counter()
    print(f"Відсортовано {N} елементів за {cur_time - ref_time} секунд!")


    print("Відсортований масив:")
    print(array)


if __name__ == "__main__":
    main()