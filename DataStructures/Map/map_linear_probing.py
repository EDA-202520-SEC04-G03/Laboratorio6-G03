import DataStructures.Map.map_functions as mf
import DataStructures.List.array_list as lt
import DataStructures.Map.map_entry as me
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

def put(my_map, key, value):
    index = mf.hash_value(my_map, key)
    capacity = my_map["capacity"]
    table = my_map["table"]

    for i in range(capacity):
        probe_index = (index + i) % capacity
        entry = lt.get_element(table, probe_index)
        entry_key = me.get_key(entry)
        if entry_key is None or entry_key == key:
            lt.change_info(table, probe_index, me.new_map_entry(key, value))
            if entry_key is None:
                my_map["size"] += 1
            return my_map

def contains(my_map, key):
    index = mf.hash_value(my_map, key)
    capacity = my_map["capacity"]
    table = my_map["table"]

    for i in range(capacity):
        probe_index = (index + i) % capacity
        entry = lt.get_element(table, probe_index)
        entry_key = me.get_key(entry)
        if entry_key is None:
            return False
        if entry_key == key:
            return True
    return False

def find_slot(my_map,key,hash_value):
    index = hash_value(my_map,key)
    i = 0
    while my_map['table'][(index + i) % my_map['capacity']] is not None:
        if my_map['table'][(index + i) % my_map['capacity']]['key'] == key:
            return (index + i) % my_map['capacity'], True
        i += 1
    return (index + i) % my_map['capacity'], False


def rehash(my_map):
    old_table = my_map['table']
    new_capacity = mf.next_prime(2 * my_map['capacity'])
    my_map['capacity'] = new_capacity
    my_map['prime'] = mf.next_prime(new_capacity + 1)
    my_map['scale'] = mf.random.randint(1, my_map['prime'] - 1)
    my_map['shift'] = mf.random.randint(0, my_map['prime'] - 1)
    my_map['table'] = [None] * new_capacity
    my_map['size'] = 0

    for entry in old_table:
        if entry is not None:
            index, found = find_slot(my_map, entry['key'], mf.hash_value)
            my_map['table'][index] = entry
            my_map['size'] += 1
            
def get(my_map,key):
    index, found = find_slot(my_map, key, mf.hash_value)
    if found:
        return my_map['table'][index]['value']
    else:
        return None
    
    
    
def remove(my_map,key):
    index, found = find_slot(my_map, key, mf.hash_value)
    if found:
        my_map['table'][index] = None
        my_map['size'] -= 1
        return True
    else:
        return False
    
def size(my_map):
    return my_map['size']

def key_set(my_map):

    keys = lt.new_list()
    table = my_map["table"]
    m = lt.size(table)
    pos = 0
    while pos < m:
        entry = lt.get_element(table, pos)
        k = me.get_key(entry)
        if k is not None:
            lt.add_last(keys, k)
        pos += 1
    return keys

def is_empty(my_map):
    return my_map["size"] == 0

