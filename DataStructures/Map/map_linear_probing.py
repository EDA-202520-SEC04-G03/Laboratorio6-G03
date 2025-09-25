import map_functions as mf

def find_slot(my_map,key,hash_value):
    index = hash_value(my_map,key)
    i = 0
    while my_map['entries'][(index + i) % my_map['capacity']] is not None:
        if my_map['entries'][(index + i) % my_map['capacity']]['key'] == key:
            return (index + i) % my_map['capacity'], True
        i += 1
    return (index + i) % my_map['capacity'], False


def rehash(my_map):
    old_entries = my_map['entries']
    new_capacity = mf.next_prime(2 * my_map['capacity'])
    my_map['capacity'] = new_capacity
    my_map['prime'] = mf.next_prime(new_capacity + 1)
    my_map['scale'] = mf.random.randint(1, my_map['prime'] - 1)
    my_map['shift'] = mf.random.randint(0, my_map['prime'] - 1)
    my_map['entries'] = [None] * new_capacity
    my_map['size'] = 0

    for entry in old_entries:
        if entry is not None:
            index, found = find_slot(my_map, entry['key'], mf.hash_value)
            my_map['entries'][index] = entry
            my_map['size'] += 1
            
def get(my_map,key):
    index, found = find_slot(my_map, key, mf.hash_value)
    if found:
        return my_map['entries'][index]['value']
    else:
        return None
    
    
    
def remove(my_map,key):
    index, found = find_slot(my_map, key, mf.hash_value)
    if found:
        my_map['entries'][index] = None
        my_map['size'] -= 1
        return True
    else:
        return False
    
def size(my_map):
    return my_map['size']

