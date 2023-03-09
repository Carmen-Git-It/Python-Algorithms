#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

def merge(values, left_start, right_start, right_end, empty_list):
    left_ptr = left_start
    right_ptr = right_start
    empty_list_index = left_ptr

    while(left_ptr < right_start) and (right_ptr <= right_end):
        if values[left_ptr] <= values[right_ptr]:
            empty_list[empty_list_index] = values[left_ptr]
            empty_list_index += 1
            left_ptr += 1
        else:
            empty_list[empty_list_index] = values[right_ptr]
            empty_list_index += 1
            right_ptr += 1

    while left_ptr < right_start:
        empty_list[empty_list_index] = values[left_ptr]
        empty_list_index += 1
        left_ptr += 1

    while right_ptr <= right_end:
        empty_list[empty_list_index] = values[right_ptr]
        empty_list_index += 1
        right_ptr += 1

    for i in range(left_start, right_end + 1):
        values[i] = empty_list[i]


def recursive_merge_sort(values, start, end, empty_list):
    if start < end:
        mid = (start + end) // 2
        recursive_merge_sort(values, start, mid, empty_list)
        recursive_merge_sort(values, mid + 1, end, empty_list)
        merge(values, start, mid + 1, end, empty_list)


def merge_sort(values):
    empty_list = [0] * len(values)

    recursive_merge_sort(values, 0, len(values) - 1, empty_list)
