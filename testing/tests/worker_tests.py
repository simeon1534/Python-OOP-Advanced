from worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Simeon', 1000, 10)

    def test_worker_is_initialised_with_name_salary_energy(self):
        self.assertEqual(self.worker.name, 'Simeon')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 10)

    def test_energy_is_increased_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy ,1 + old_energy)

    def test_error_when_worker_work_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_error_when_worker_work_with_negative_energy(self):
        self.worker.energy = -1
        with self.assertRaises(Exception):
            self.worker.work()

    def test_incrementing_money_after_work(self):
        old_money = self.worker.money
        self.worker.work()
        new_money = self.worker.money
        self.assertEqual(new_money , self.worker.salary + old_money)

    def test_energy_is_decreased_after_work(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy, old_energy - 1)

    def test_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(info, f"Simeon has saved 0 money.")


if __name__ == '__main__':
    unittest.main()
