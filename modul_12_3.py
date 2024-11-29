
import unittest
import inspect
import runner_2


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name = runner_2.Runner('Кристина')
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name_1 = runner_2.Runner('Кира')
        for i in range(10):
            name_1.run()
        self.assertEqual(name_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        name_2 = runner_2.Runner('Татьяна')
        name_3 = runner_2.Runner('Лиза')
        for i in range(10):
            name_2.walk()
            name_3.run()
        self.assertNotEqual(name_2.distance, name_3.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_2.Runner('Усэйн', 10)
        self.runner_2 = runner_2.Runner('Андрей', 9)
        self.runner_3 = runner_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for i in cls.all_results:
            print()
            print(f'{i}:')
            print({key: str(value) for key, value in cls.all_results[i].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_name(self):
        tour = runner_2.Tournament(90, self.runner_1, self.runner_3)
        result = tour.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_name_2(self):
        tour = runner_2.Tournament(90, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_name_3(self):
        tour = runner_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)


if __name__ == "__main__":
    unittest.main()
