import unittest
from hash_table_chaining import *

class Hash_Tests(unittest.TestCase):

    def test_table(self):
        my_table = empty_hash_table()
        self.assertEqual(my_table, HashTable([None]*8, 0, 0))
        self.assertEqual(repr(my_table),
                         'Table Size: 8, Num of Items: 0, Collisions: 0, Table: '
                         '[None, None, None, None, None, None, None, None]')

    def test_insert(self):
        my_table = empty_hash_table()
        insert(my_table, 5, 10)
        insert(my_table, 13, 16)
        self.assertEqual(my_table.lst[5], linked_list.Pair((13, 16), linked_list.Pair((5, 10), None)))
        self.assertEqual(my_table.items, 2)
        insert(my_table, 13, 8)
        self.assertEqual(my_table.lst[5], linked_list.Pair((13, 8), linked_list.Pair((5, 10), None)))
        self.assertEqual(my_table.items, 2)
        self.assertEqual(my_table.collisions, 2)
        insert(my_table, 21, 18)
        self.assertEqual(my_table.collisions, 3)

    def test_get(self):
        my_table = empty_hash_table()
        self.assertRaises(LookupError, get, my_table, 5)
        insert(my_table, 2, 18)
        insert(my_table, 10, 19)
        val = get(my_table, 10)
        val1 = get(my_table, 2)
        self.assertEqual(val, 19)
        self.assertEqual(val1, 18)
        self.assertRaises(LookupError, get, my_table, 5)

    def test_remove1(self):
        my_table = empty_hash_table()
        self.assertRaises(LookupError, remove, my_table, 4)
        insert(my_table, 5, 10)
        insert(my_table, 13, 16)
        remove(my_table, 5)
        self.assertEqual(my_table.lst[5], linked_list.Pair((13, 16), None))
        self.assertRaises(LookupError, remove, my_table, 5)

    def test_size(self):
        my_table = empty_hash_table()
        self.assertEqual(size(my_table), 0)
        insert(my_table, 5, 10)
        insert(my_table, 13, 16)
        self.assertEqual(size(my_table), 2)

    def test_load(self):
        my_table = empty_hash_table()
        self.assertEqual(load_factor(my_table), 0)
        insert(my_table, 'hey', 2)
        for i in range(14):
            insert(my_table, i, 2*i)
        insert(my_table, 'hello', 2)
        insert(my_table, 'hey', 2)
        insert(my_table, 'hi', 2)
        self.assertEqual(load_factor(my_table), 17/16)

    def test_collisions(self):
        my_table = empty_hash_table()
        self.assertEqual(collisions(my_table), 0)
        insert(my_table, 5, 10)
        insert(my_table, 13, 16)
        remove(my_table, 13)
        self.assertEqual(collisions(my_table), 1)

if __name__ == '__main__':
    unittest.main()