import linked_list

# a HashTable is a array list and a number of elements in the table
class HashTable:
    def __init__(self, lst, items, collisions):
        self.lst = lst
        self.items = items
        self.table_size = len(lst)
        self.collisions = collisions

    def __eq__(self, other):
        return (type(other) == HashTable and
                self.items == other.items and
                self.lst == other.lst and
                self.collisions == other.collisions)

    def __repr__(self):
        return ("Table Size: {}, Num of Items: {}, Collisions: {}, Table: {}"
                .format(self.table_size, self.items, self.collisions, self.lst))


# -> HashTable
# Creates an empty HashTable
def empty_hash_table():
    empty_lst = [None] * 8
    return HashTable(empty_lst, 0, 0)

# HashTable -> HashTable
# Doubles the length of the table and rehashes every value
def rehash(table):
    new_lst = [None]*(table.table_size*2)
    for idx in range(len(table.lst)):
        new_lst[idx] = table.lst[idx]
    table.lst = [None]*(table.table_size*2)
    table.collisions = 0
    table.items = 0
    table.table_size = table.table_size*2
    for idx in range(len(new_lst)):
        if new_lst[idx] != None:
            linked = new_lst[idx]
            for i in range(linked_list.length(linked)):
                pair = linked_list.get(linked, i)
                insert(table, pair[0], pair[1])
    return table

# HashTable value value -> HashTable
#
def insert(table, key, value):
    index = hash(key)%table.table_size
    if table.lst[index] is None:
        table.lst[index] = linked_list.add(table.lst[index], 0, (key, value))
        table.items += 1
    else:
        dup = False
        linked = table.lst[index]
        for i in range(linked_list.length(linked)):
            if linked_list.get(linked, i)[0] == key:
                table.collisions += 1
                table.lst[index] = linked_list.set(linked, i, (key, value))
                dup = True
        if dup == False:
            table.collisions += 1
            table.lst[index] = linked_list.add(linked, 0, (key, value))
            table.items += 1
    if (table.items/ table.table_size) > 1.5:
        rehash(table)
    return table

# HashTable value -> value
# Takes a HashTable and returns the value at the given key, raise error if key is not in the table
def get(table, key):
    index = hash(key) % table.table_size
    if table.lst[index] is None:
        raise LookupError
    else:
        linked = table.lst[index]
        for i in range(linked_list.length(table.lst[index])):
            if linked_list.get(linked, i)[0] == key:
                return linked_list.get(linked, i)
    raise LookupError

# HashTable value -> HashTable
# removes the value associated with the key, raises error if no key exists in table
def remove(table, key):
    index = hash(key) % table.table_size
    if table.lst[index] is None:
        raise LookupError
    elif table.lst[index].first[0] == key:
        val, table.lst[index] = linked_list.remove(table.lst[index], 0)
        table.items -= 1
    else:
        linked = table.lst[index]
        removed = False
        for i in range(linked_list.length(linked)):
            if linked_list.get(linked, i)[0] == key:
                val, table.lst[index] = linked_list.remove(table.lst[index], i)
                table.items -= 1
                removed = True
        if removed == False:
            raise LookupError
    return table

# HashTable -> Int
# Returns the number of items in the table
def size(table):
    return table.items

# HashTable -> Float
# Returns the load factor of the table
def load_factor(table):
    return table.items / table.table_size

# HashTable -> Int
# returns the number of collisions in the table
def collisions(table):
    return table.collisions