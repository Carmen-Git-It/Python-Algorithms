#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

def insertion_sort(values):
    size = len(values)

    for i in range(1, size):
        temp = values[i]

        j = i
        while j > 0 and values[j - 1] > temp:
            values[j] = values[j - 1]
            j -= 1

        values[j] = temp
