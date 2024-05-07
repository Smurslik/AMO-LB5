def sort(arr):
    n = 1
    while n < len(arr):
        for i in range(n):
            if arr[i] > arr[n]:
                arr.insert(i , arr.pop(n))
        n += 1
    return arr, n
masiv = [1,34,3,67,98675,345,41,8]


def shellsort(arr):
    gap = len(arr)//2
    comparisons = 0
    swap = 0
    while gap>0 :
        for i in range(0, len(arr) - gap):
            comparisons += 1
            if arr[i] > arr[i+gap]:
                masiv[i], masiv[i+gap] = masiv[i+gap], masiv[i]
                swap += 1
            print(f'{masiv}, порівнянь: {comparisons} перестанов: {swap}')
        gap //= 2
    return ""

print(shellsort(masiv))
