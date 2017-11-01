


def binary_search(arr, t, offset = 0):
    l = 0
    r = len(arr) - 1
    if l > r:
        return -1
    m = ((l + r)//2)
    if arr[m] < t:
        offset = m +1
        if offset > len(arr)-1:
            return -1
        return binary_search(arr[offset:], t, offset)+offset
    elif arr[m] > t:

        return binary_search(arr[:m], t, offset)

    return m

print(binary_search([11,51],12))