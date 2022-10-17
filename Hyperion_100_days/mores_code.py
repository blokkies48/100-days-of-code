# Creating both list
code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphabet = list(map(chr, range(97, 123))) # Generating alphabet using the ascii alphabet value http://sticksandstones.kstrom.com/appen.html

# Casting them to a dictionary by zipping them together
code_dictionary = dict(zip(alphabet,code))

# Function used.
def read_morse(words): 
    return_list = [] # Setting return list
    for word in words: # Looping over words in words
        return_string = "" # With each loop of words the return string will be set to empty
        for letter in word: # Looping over letter in the word
            return_string += code_dictionary[letter] # Adding the value from dictionary to the string

        if return_string not in return_list: # Checking if the new string is in the empty list.
            return_list.append(return_string) # Appending to the list
    return len(return_list) # Returning the length of the list
    

words = ["gin","zen","gig","msg","for","saf"] # Creating words list

    
print(read_morse(words))
