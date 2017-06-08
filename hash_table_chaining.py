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
    empty_lst = [[] for a in range(8)]
    return HashTable(empty_lst, 0, 0)

# HashTable -> HashTable
# Doubles the length of the table and rehashes every value
def rehash(table):
    new_lst = [[] for a in range(table.table_size*2)]
    for idx in range(len(table.lst)):
        new_lst[idx] = table.lst[idx]
    table.lst = [[] for a in range(table.table_size*2)]
    table.collisions = 0
    table.items = 0
    table.table_size = table.table_size*2
    for idx in range(len(new_lst)):
        if new_lst[idx] != []:
            linked = new_lst[idx]
            for i in range(len(linked)):
                pair = linked[i]
                insert(table, pair[0], pair[1])
    return table

# HashTable value value -> HashTable
# Inserts a value into the hash table based on its key
def insert(table, key, value):
    index = hash(key)%table.table_size
    if table.lst[index] == []:
        table.lst[index].append((key, value))
        table.items += 1
    else:
        dup = False
        linked = table.lst[index]
        for i in range(len(linked)):
            if linked[i][0] == key:
                table.collisions += 1
                table.lst[index][i] = (key, value)
                dup = True
                break
        if dup == False:
            table.collisions += 1
            table.lst[index].append((key, value))
            table.items += 1
    if (table.items/ table.table_size) > 1.5:
        rehash(table)
    return table

# HashTable value -> value
# Takes a HashTable and returns the value at the given key, raise error if key is not in the table
def get(table, key):
    index = hash(key) % table.table_size
    if table.lst[index] == []:
        raise LookupError
    else:
        linked = table.lst[index]
        for i in range(len(linked)):
            if linked[i][0] == key:
                return linked[i][1]
    raise LookupError

# HashTable value -> HashTable
# removes the value associated with the key, raises error if no key exists in table
def remove(table, key):
    index = hash(key) % table.table_size
    if table.lst[index] == []:
        raise LookupError
    else:
        linked = table.lst[index]
        for i in range(len(linked)):
            if linked[i][0] == key:
                table.lst[index].remove(linked[i])
                table.items -= 1
                return table
        raise LookupError

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