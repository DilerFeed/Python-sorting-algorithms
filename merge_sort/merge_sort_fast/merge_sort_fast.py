import merge_sort_light
import time

if __name__ == "__main__":
    N = int(input("Введіть кількість елементів масиву: "))
    sorting_array = merge_sort_light.get_array(N)
    ref_time = time.perf_counter()
    merge_sort_light.merge_sort(sorting_array)
    cur_time = time.perf_counter()
    print(f"Відсортовано {N} елементів за {cur_time - ref_time} секунд!")
    