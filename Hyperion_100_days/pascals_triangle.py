def pascals_triangle(num_rows):
    return_list = [] # List that is going to be returned

    for index in range(1,num_rows + 1): # Loop used to create list objects
        row = [1 for _ in range(index)] # List comp to generate list of 1s
        if len(row) > 2: # If list length is greater than two then code will be used on the list. Because list up to 2 is [1] and [1,1]
            for i in range(len(row)): # Looping over list and crying a bit
                row[1] = index - 1 # Setting the 2 position to equal the index of the list
                row[index - len(row) - 2] = index - 1 # Setting the 2nd last position to equal the index of the list
                if len(row) > 3 and (1 < i and i < len(row) - 2): # Checking if list is greater than 3 and making user i is in the correct range
                    # getting the pervious list by return_list[index - 2] and getting the index i and i - 1
                    row[i] = return_list[index - 2][i] + return_list[index - 2][i - 1] # The number at the index will equal the pervious's list number at same index plus the pervious item
        return_list.append(row) # Appending lists to return list          
        
    return return_list # Returning list

print(pascals_triangle(7))

