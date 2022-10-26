from groups import Group, Person
import unittest


class TestPerson(unittest.TestCase):
    def test_initialising_person_obj(self):
        Person('Ivan', 'Ivanov')

    def test_adding_names_logic(self):
        person = Person('Ivan', 'Ivanov')
        another_person = Person('Dimityr', 'Dimitrov')
        result_person = person + another_person
        string_name = result_person.name + ' ' + result_person.surname
        self.assertEqual(string_name, 'Ivan Dimitrov')

    def test_repr_method(self):
        person = Person('Ivan', 'Ivanov')
        self.assertEqual(repr(person), person.name + ' ' + person.surname)


class TestGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.p0 = Person('Aliko', 'Dangote')
        self.p1 = Person('Bill', 'Gates')
        self.p2 = Person('Warren', 'Buffet')
        self.p3 = Person('Elon', 'Musk')
        self.p4 = Person('Warren', 'Musk')

    def test_initialising_group_obj(self):
        Group('__VIP__', [self.p0, self.p1, self.p2])

    def test_how_many_people_in_a_group(self):
        g1 = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(len(g1), 3)

    def test_repr_method_for_group(self):
        g1 = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(repr(g1), f"Group __VIP__ with members Aliko Dangote,"
                                   f" Bill Gates, Warren Buffet")

    def test_group_add_group(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        second_group = Group('Special', [self.p3, self.p4])
        third_goup = first_group + second_group
        self.assertEqual(third_goup.name, 'todo')
        self.assertEqual(repr(third_goup), f"Group todo with members Aliko Dangote,"
                                           f" Bill Gates, Warren Buffet, Elon Musk, Warren Musk")

    def test_when_iterating_over_people_in_group_or_indexing_group(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        second_group = Group('Special', [self.p3, self.p4])
        third_goup = first_group + second_group
        self.assertEqual(third_goup[1], 'Person 1: Bill Gates')
        for idx,person in enumerate(third_goup):
            if idx == 3:
                self.assertEqual(person, 'Person 3: Elon Musk')
                break

if __name__ == '__main__':
    unittest.main()
