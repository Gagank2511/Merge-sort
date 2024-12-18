from merge_sort import merge_sort, run_test
import random

# Now testing the larger dataset
large_data = [random.randint(1, 10000) for _ in range(1000)]
sorted_large_data = merge_sort(large_data)
if sorted_large_data == sorted(large_data):
    print("Large dataset test has passed.")
else:
    print("Large dataset test has failed.")


if __name__ == "__main__":
    numbers = [23, 43, 56, 2, 1, 67, 26, 99]
    sorted_lst = merge_sort(numbers)
    print("Sorted array:", sorted_lst)

    run_test()