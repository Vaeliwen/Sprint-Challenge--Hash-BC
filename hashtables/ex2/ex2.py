#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    route[0] = hash_table_retrieve(hashtable, "NONE")

    current = 1

    while route[-2] == None:
        route[current] = hash_table_retrieve(hashtable, route[current-1])
        current += 1
    
    route.pop()



    return route    
        
        

