from extended_list import IntegerList
import unittest


class ListTests(unittest.TestCase):
    def setUp(self):
        self.int_list = IntegerList()

    def test_constructor(self):
        self.assertEqual(self.int_list.get_data(), [])

    def test_add_integer(self):
        self.int_list.add(6)
        self.assertEqual(self.int_list.get_data(), [6])

    def test_add_not_integer(self):
        with self.assertRaises(ValueError):
            self.int_list.add('7')

    def test_remove_index_out_of_range(self):
        with self.assertRaises(IndexError):
            for i in range(6):
                self.int_list.add(i)
            self.int_list.remove_index(6)

    def test_remove_index_in_range(self):
        for i in range(6):
            self.int_list.add(i)
        self.int_list.remove_index(-1)
        self.assertEqual(self.int_list.get_data(), [0, 1, 2, 3, 4])

    def test_get_index_out_of_range(self):
        with self.assertRaises(IndexError):
            for i in range(6):
                self.int_list.add(i)
            self.int_list.get(6)

    def test_get_index_in_range(self):
        for i in range(6):
            self.int_list.add(i)
        self.assertEqual(self.int_list.get(5), 5)

    def test_insert_out_of_range(self):
        with self.assertRaises(IndexError):
            for i in range(6):
                self.int_list.add(i)
            self.int_list.insert(6, 76)

    def test_insert_in_range_wrong_type(self):
        with self.assertRaises(ValueError):
            for i in range(6):
                self.int_list.add(i)
            self.int_list.insert(5, 76.8)

    def test_insert_in_range_correct(self):
        for i in range(6):
            self.int_list.add(i)
        self.int_list.insert(5, 76)
        self.assertEqual(self.int_list.get_data(), [0, 1, 2, 3, 4, 76, 5])

    def test_get_biggest(self):
        for i in range(6):
            self.int_list.add(i)
        the_biggest = self.int_list.get_biggest()
        self.assertEqual(the_biggest, 5)

    def test_get_index(self):
        for i in range(6):
            self.int_list.add(i)
        self.assertEqual(self.int_list.get_index(5), 5)


if __name__ == '__main__':
    unittest.main()
