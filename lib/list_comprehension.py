#!/usr/bin/env python3

def return_evens(num_list):
    even_elements = [num for num in num_list if num % 2 == 0]
    return even_elements

return_evens([0, 1, 3, 5, 7, 8, 9])
    
def make_exclamation(sentence_list):
    modified_list = list()
    for sentence in sentence_list:
        modified_list.append(sentence + '!')
    return modified_list

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
        