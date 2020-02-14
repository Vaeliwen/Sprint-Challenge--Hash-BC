#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    index = 0
    answer = None

    for i in weights:
        hash_table_insert(ht, i, index)
        index += 1

    for i in weights:
        j = None

        if hash_table_retrieve(ht, limit - i):
            j = limit - i
            k = hash_table_retrieve(ht, limit - i)
            l = hash_table_retrieve(ht, i)
        
        if j == None:
            pass
        elif i == j:
            answer = (l, k-1)
        else:
            answer = (l, k)

        
    print(answer)
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
