def magic_sorting(arr1,arr2): # Funny func
    return_arr = [] # Return of the list
    for num in arr2: # Looping over the sorting list
        for number in arr1: # Looping over the list that has to be sorted
            if number == num: # If number in the list to be sorted is = to the number in the sorting list
                return_arr.append(num) # Append to the returned list

    left_overs = [i for i in arr1 if i not in return_arr]  # Getting the left over numbers using list comprehension
    left_overs.sort() # Sorting those numbers  
    return return_arr + left_overs # Returning the new list plus the sorted left over numbers.


print(magic_sorting([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
print(magic_sorting([28,6,22,8,44,17],[22,28,8,6]))
