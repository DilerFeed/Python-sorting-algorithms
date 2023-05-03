import random
import time

def main():
    # Заповнюємо масив для сортування
    type = 2
    N = int(input("Введіть кількість елементів масиву: "))
    array = []
    # Випадкове заповнення дуже великими елементами (найгірший випадок)
    if type == 1:
        for i in range(N):
            array.append(random.randint(0,(N**2)))
    # Випадкове заповнення маленькими елементами (середній випадок)
    elif type == 2:
        for i in range(N):
            array.append(random.randint(0, N))
    # Випадкове заповнення маленькими однаковими елементами (найкращий випадок)
    elif type == 3:
        num = random.randint(0, N)
        for i in range(N):
            array.append(num)

    """
    print("-----------------")
    print("Початковий масив:")
    print(array)
    """

    ref_time = time.perf_counter()

    # Сортування підрахуванням
    cnt = [0] * (max(array) + 1)  # Генерація списку нулів довжиною у максимальний елемент списку array
    for item in array:
        cnt[item] += 1   # Коли ми зустрічаємо число у списку, збільшуємо його значення на 1
    # Додаємо count раз число num в результат
    result = [num for num, count in enumerate(cnt) for i in range(count)]

    # Вивести дані по часу сортування всіх елементів
    cur_time = time.perf_counter()
    print(f"Відсортовано {N} елементів за {cur_time - ref_time} секунд!")

    """
    print("Відсортований масив:")
    print(result)
    """

if __name__ == "__main__":
    main()
