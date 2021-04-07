"""Removes single letters from dictionary file."""
import load_dictionary

word_list = load_dictionary.load('greentea_dictionary.txt')

def clean_dictionary():

    word_list_clean = []

    for word in word_list:
        if len(word) > 2:
            word_list_clean.append(word)
        else:
            continue
    return word_list_clean

new_list = clean_dictionary()

print(len(word_list))
print(len(new_list))
