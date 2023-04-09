import random
import time
import numpy
import cython
from cpython cimport array
import array


# Сортування злиттям
@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def merge_sort(A:int) -> int:
    # У випадку, коли масиви = 0 або 1, повертаємо їх без сортування
    if len(A) == 1 or len(A) == 0:
        return A
    # Рекурсивно викликаємо функцію для лівої та правої частини
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])
    cdef int n = 0
    cdef int m = 0
    cdef int k = 0
    # Копіюємо частини в один масив
    C:int = [0] * (len(L) + len(R))
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

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def get_array(N:int) -> int:
    # Заповнюємо масив для сортування
    type = 1
    our_array:int = []
    # Випадково
    if type == 1:
        for i in range(N):
            our_array.append(random.randint(0,(N**2)))
    # Відсортований
    elif type == 2:
        for i in range(N):
            our_array.append(int(i))
    # Відсортований у зворотньому порядку
    elif type == 3:
        for i in range(N):
            our_array.append(int(i))
        our_array = our_array[::-1]
    return our_array
