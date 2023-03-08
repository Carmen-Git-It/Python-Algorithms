#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

def binary_search(values, element):
    low = 0
    high = len(values)

    while low < high:
        mid = (low + high) // 2

        if element == values[mid]:
            return mid
        elif element < values[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None
