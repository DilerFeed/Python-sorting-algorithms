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
    ref_time = time.perf_counter()
    # Для кожного елементу масиву
    for step in range(N):
        min_idx = step
        # Шукаємо серед елементів, окрім ключа, ті які менше ключа
        for i in range(step + 1, N):
            # Коли знайшли, ...
            if array[i] < array[min_idx]:
                # ... вибираємо цей елемент, як ключ
                min_idx = i
        # Ставимо його в правильну позицію
        (array[step], array[min_idx]) = (array[min_idx], array[step])

        # Вивести дані по часу сортування по 10 елементів
        cur_time = time.perf_counter()
        if (step + 1) % 10 == 0:
            print(f"Відсортовано {step + 1} елементів за {cur_time - ref_time} секунд!")

    """
    # Вивести дані по часу сортування всіх елементів
    cur_time = time.perf_counter()
    print(f"Відсортовано {N} елементів за {cur_time - ref_time} секунд!")
    """

    print("Відсортований масив:")
    print(array)


if __name__ == "__main__":
    main()