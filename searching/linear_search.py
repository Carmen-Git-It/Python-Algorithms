#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

def linear_search(values, element):
    for x in range(len(values)):
        if values[x] == element:
            return x
    return None
