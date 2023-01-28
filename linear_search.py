pos = -1


def linear_search(list, n):
    for value in range(0, len(list)):
        if list[value] == n:
            globals()['pos'] = value
            return True
    return False

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1


list = [2, 5, 67, 56, 76, 78]
n = 76

if linear_search(list, n):
    print('Found at', pos + 1)
else:
    print('Not found')
