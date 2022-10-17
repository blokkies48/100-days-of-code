def spicy_sorting(arr):
    return_arr1 = []
    return_arr2 = []
    for item in arr:
        if item < 0:
            return_arr1.append(item)
        else:
            return_arr2.append(item)

    return return_arr2 + return_arr1

arr1 = [1, -1, 3, 2, -7, -5, 11, 6 ]

print(spicy_sorting(arr1))


arr = [1, -1, 3, 2, -7, -5, 11, 6]

def sorted(arr):
    return [x for x in arr if x > 0] + [x for x in arr if x < 0]

print(sorted(arr))