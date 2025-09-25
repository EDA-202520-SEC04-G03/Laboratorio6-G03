import map_functions as mf
import map_entry as me
import random

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))

    hash_table = {
        "prime" : prime,
        "capacity" : capacity,
        "scale" : random.randrange(1, prime - 1),
        "shift" : random.randrange(0, prime - 1),
        "table" : map.entry * capacity,
        "current_factor" : 0,
        "limit_factor" : load_factor,
        "size" : 0
    }

    return hash_table

my_table = new_map(5, 0.5)
print(my_table)