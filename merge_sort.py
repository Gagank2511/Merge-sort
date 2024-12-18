def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the arrays into half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Now Merge the sorted half
    return merge(left, right)


def merge(left, right):
    result = []
    left_index = right_index = 0

    # Now merge the two arrays while maintaining sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Now if there are any remaining elements in left, add them to the left
    result.extend(left[left_index:])

    # Now if there are any remaining elements in right, add them to the right
    result.extend(right[right_index:])

    return result


def run_test():
    test_cases = [
        ([23, 43, 56, 2, 1, 67, 26, 99], [1, 2, 23, 26, 43, 56, 67, 99]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([2, 3, 4, 5, 6], [2, 3, 4, 5, 6]),
        ([26], [26]),
        ([], []),
    ]

    for i, (input_data, expected_result) in enumerate(test_cases):
        output = merge_sort(input_data)
        if output == expected_result:
            print(f"Test case {i + 1} has passed.")
        else:
            print(f"Test case {i + 1} has failed: expected {expected_result}, got {output}")




