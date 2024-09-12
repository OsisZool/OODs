import random
comparecount = 0

def binary_search(arr, low, high, x):
    global comparecount
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            comparecount += 1
            print("comparecount = ", comparecount, "low = ", low, "high =", mid - 1)
            return binary_search(arr, low, mid - 1, x)
        else:
            comparecount += 1
            print("comparecount = ", comparecount, "low = ", mid + 1, "high =", high)
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

def sequential_search(arr, x):
    global comparecount
    for i in arr:
        comparecount += 1
        if i == x:
            return comparecount
    return -1

datcount = 100000
arr = sorted([random.randint(1, 10000000) for i in range(datcount)])

# Set the key to a value that is not in the list
x = -9999

print("key =", x)
print("data len =", len(arr))

# Uncomment for binary search
result = binary_search(arr, 0, len(arr) - 1, x)

# Comment out for sequential search
# result = sequential_search(arr, x)

print("compare count =", comparecount)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
