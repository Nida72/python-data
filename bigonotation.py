#Linear Search – O(n)
#1
arr = [4, 2, 9, 1, 5]
target = 9
result = linear_search(arr, target) # type: ignore
print("Found at index:", result)

#2
def linear_search(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

#Binary Search – O(log n)

def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

#2
arr = [2,8,0,4] 
target = 4
result = binary_search(arr, target)
print("Found at index:", result)
