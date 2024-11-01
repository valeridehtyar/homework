from module_2_5 import result1, result2


def singl_root_words(roo_word, *other_words) :
    same_words = []

    for  word  in other_words :
        if roo_word.upper() in word.upper() or word.upper() in roo_word.upper() :
            same_words.append(word)
    return same_words


result1 = singl_root_words('rich','richiest','orichalcum','cheers','richies')
result2 = singl_root_words('Disablement','Able','Mable','Disable','Bagel')

print(result1)
print(result2)