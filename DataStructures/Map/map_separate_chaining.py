import map_functions as mf
import DataStructures.List.single_linked_list as lt
import DataStructures.List.array_list as al
import map_entry as me
import random



def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))

    table = lt.new_list()
    for _ in range(capacity):
        lt.add_last(table, me.new_map_entry(None, None))

    hash_table = {
        "prime" : prime,
        "capacity" : capacity,
        "scale" : random.randrange(1, prime - 1),
        "shift" : random.randrange(0, prime - 1),
        "table" : table,
        "current_factor" : 0,
        "limit_factor" : load_factor,
        "size" : 0
    }

    return hash_table

def contains(my_map, key):
    index = mf.hash_value(my_map, key)
    table = my_map["table"]

    bucket = lt.get_element(table, index)
    size_bucket = lt.size(bucket)

    if lt.is_empty(bucket):
        return False
    
    for i in range(size_bucket):
        entry = lt.get_element(bucket, i)
        entry_key = me.get_key(entry)
        if entry_key == key:
            return True
    return False

def size(my_map):
    return my_map['size']

def value_set(my_map):
    table = my_map["table"]
    keys = al.new_list()

    if size(my_map) == 0:
        return keys
    
    for pos in range(lt.size(table)):
        bucket = lt.get_element(table, pos)
        size_bucket = lt.size(bucket) 
        if not lt.is_empty(bucket):
            for i in range(size_bucket):
                entry = lt.get_element(bucket, i)            
                al.add_last(keys, entry["value"])
    return keys