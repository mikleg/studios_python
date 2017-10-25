def binary_search(arr, t):
    l = 0
    r=len(arr) - 1
    while True:
        if l > r:
            return -1
        m = ((l + r)//2)
        print(m)
        if arr[m] < t:
            l = m + 1
        elif arr[m] > t:
            r = m - 1
        else:
            break
    return m
