from __future__ import print_function

"""Determine whether words are a palindrome in a dictionary and add them into a list"""

import load_dictionary

word_list = load_dictionary.load('greentea_dictionary.txt')

def palindrome(word):
    
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else: 
        return palindrome(word[1:-1])

def palindrome_dictionary(words):
    palin_list = []

    for word in words:
        if palindrome(word) == False:
            continue 
        else:
            palin_list.append(word)
    
    return palin_list

dict_palindromes = palindrome_dictionary(word_list)

print("There are a total of {} palindromes in your dictionary. They are:".format(len(dict_palindromes)))
print(*dict_palindromes, sep='\n')