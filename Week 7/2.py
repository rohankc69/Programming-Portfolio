def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))  

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  

def letters_in_one_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  


def test_functions():
    word1 = "rohan"
    word2 = "kc"

    print("Letters in at least one of the words:", letters_in_either(word1, word2))
    print("Letters in both words:", letters_in_both(word1, word2))
    print("Letters in either but not both:", letters_in_one_but_not_both(word1, word2))


test_functions()