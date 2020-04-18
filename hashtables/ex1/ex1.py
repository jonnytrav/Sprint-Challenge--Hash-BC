#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # store each value as index
    # key is the weight
    # limit - weight gives us both indexes that add up to limit
    index = 0
    for w in weights:
        hash_table_insert(ht, w, index)
        index += 1

    for i in range(length):
        target_index = hash_table_retrieve(ht, limit - weights[i])
        if target_index:
            if i > target_index:
                return (i, target_index)
            else:
                return (target_index, i)

    # needed_val =
    # if ht.hash_table_retrieve(needed_val)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
