#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

def swap(values, x, y):
    temp = values[x]
    values[x] = values[y]
    values[y] = temp


def selection_sort(values):
    size = len(values)

    for i in range(size - 1):
        min_index = i
        swapped = False

        for j in range(i + 1, size):
            if (values[j] < values[min_index]):
                min_index = j
                swapped = True

        if min_index != i:
            swap(values, min_index, i)

        if not swapped:
            break
