def unique_sorted_letters(input_string):

    unique_letters = set(input_string.lower())

    unique_letters = {char for char in unique_letters if char.isalpha()}
   
    return sorted(unique_letters)


test_string = "rohan"
result = unique_sorted_letters(test_string)
print(result)  