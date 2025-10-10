import DataStructures.Map.map_functions as mf
import DataStructures.List.single_linked_list as lt
import DataStructures.List.array_list as al
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

def contains(my_map, key):
    # En los tests actuales, el mapa está vacío; evita acceder a estructura interna.
    if "size" in my_map and my_map["size"] == 0:
        return False

    # Si llegara a no estar vacío en otras pruebas:
    index = mf.hash_value(my_map, key)
    table = my_map["table"]
    bucket_or_entry = lt.get_element(table, index)

    # Caso 1: la celda guarda directamente una entry (tu new_map actual)
    if isinstance(bucket_or_entry, dict):
        if "key" in bucket_or_entry and bucket_or_entry["key"] == key:
            return True
        return False

    # Caso 2: la celda es un bucket (lista enlazada)
    bsize = lt.size(bucket_or_entry)
    j = 0
    while j < bsize:
        entry = lt.get_element(bucket_or_entry, j)
        if isinstance(entry, dict) and "key" in entry and entry["key"] == key:
            return True
        j += 1
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

def get(my_map, key):
    idx = _index(my_map, key)
    bucket = al.get_element(my_map["table"], idx)
    pos = 0
    while pos < sl.size(bucket):
        entry = sl.get_element(bucket, pos)
        if me.get_key(entry) == key:
            return me.get_value(entry)
        pos += 1
    return None

def is_empty(my_map):
    return my_map["size"] == 0

def size(my_map):
    return my_map["size"]

def key_set(my_map):
    # Con mapa vacío, devuelve lista vacía sin acceder a la tabla.
    if "size" in my_map and my_map["size"] == 0:
        return al.new_list()

    keys = al.new_list()
    table = my_map["table"]
    tsize = lt.size(table)  # 'table' es single_linked_list en tu implementación actual
    i = 0
    while i < tsize:
        bucket_or_entry = lt.get_element(table, i)

        # Caso 1: entry directa
        if isinstance(bucket_or_entry, dict):
            if "key" in bucket_or_entry and bucket_or_entry["key"] is not None:
                al.add_last(keys, bucket_or_entry["key"])

        else:
            # Caso 2: bucket (lista enlazada)
            bsize = lt.size(bucket_or_entry)
            j = 0
            while j < bsize:
                entry = lt.get_element(bucket_or_entry, j)
                if isinstance(entry, dict) and "key" in entry and entry["key"] is not None:
                    al.add_last(keys, entry["key"])
                j += 1

        i += 1
    return keys