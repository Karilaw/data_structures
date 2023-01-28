pos = -1


def binary_search(list, n):
    l = 0
    u = len(list) - 1

    while u > l:
        mid_index = (l + u) // 2

        if list[mid_index] == n:
            globals()['pos'] = mid_index
            return True
        else:
            if list[mid_index] < n:
                l = mid_index + 1
            else:
                u = mid_index - 1

    return False


list = [1, 2, 3, 4, 56, 67, 78, 879, 567]
n = 989

if binary_search(list, n):
    print('value found at', pos)
else:
    print('value not found')
