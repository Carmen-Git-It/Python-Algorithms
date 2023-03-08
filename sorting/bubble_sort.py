#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

def bubble_sort(values):
    size = len(values)

    for i in range(size):
        swapped = False
        for j in range(size - 1):
            if values[j] > values[j + 1]:
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp
                swapped = True
        if not swapped:
            break
