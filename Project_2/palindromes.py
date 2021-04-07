from __future__ import print_function

"""Find palindromes in given dictionary txt file."""
import load_dictionary
word_list = load_dictionary.load('greentea_dictionary.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
