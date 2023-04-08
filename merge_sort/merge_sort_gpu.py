import random
import time
from numba import jit, cuda, numba

# Для обчислення на ядрах CUDA відеокарт Nvidia (можливо підвищення швидкості на 10-25%)

def main():
    # Заповнюємо масив для сортування
    type = 1
    N = int(input("Введіть кількість елементів масиву: "))
    array = []
    # Випадково
    if type == 1:
        for i in range(N):
            array.append(random.randint(0,(N**2)))
    # Відсортований
    elif type == 2:
        for i in range(N):
            array.append(int(i))
    # Відсортований у зворотньому порядку
    elif type == 3:
        for i in range(N):
            array.append(int(i))
        array = array[::-1]

    """
    print("-----------------")
    print("Початковий масив:")
    print(array)
    """
    # Сортування злиттям
    @jit(target_backend='cuda')
    def merge_sort(A):
        # У випадку, коли масиви = 0 або 1, повертаємо їх без сортування
        if len(A) == 1 or len(A) == 0:
            return A
        # Рекурсивно викликаємо функцію для лівої та правої частини
        L = merge_sort(A[:len(A) // 2])
        R = merge_sort(A[len(A) // 2:])
        n = m = k = 0
        # Копіюємо частини в один масив
        C = [0] * (len(L) + len(R))
        # Сортуємо ліву та праву частини
        while n < len(L) and m < len(R):
            if L[n] <= R[m]:
                C[k] = L[n]
                n += 1
            else:
                C[k] = R[m]
                m += 1
            k += 1
        # Обʼєднуємо дві відсортовані частини у масиві-копії
        while n < len(L):
            C[k] = L[n]
            n += 1
            k += 1
        while m < len(R):
            C[k] = R[m]
            m += 1
            k += 1
        # Копіюємо відсортований масив-копію до оригінальної частини
        for i in range(len(A)):
            A[i] = C[i]
        # Повертаємо відсортовану частину
        return A

    ref_time = time.perf_counter()
    merge_sort(numba.typed.List(array))

    # Вивести дані по часу сортування всіх елементів
    cur_time = time.perf_counter()
    print(f"Відсортовано {N} елементів за {cur_time - ref_time} секунд!")

    """
    print("Відсортований масив:")
    print(array)
    """

if __name__ == "__main__":
    main()
