import logging
import unittest
import rt_with_exceptions

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding="utf-8", format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            object1 = rt_with_exceptions.Runner('Test', speed=-15)
            for i in range(10):
                object1.walk()
            self.assertEqual(object1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            object2 = rt_with_exceptions.Runner(5)
            for i in range(10):
                object2.run()
            self.assertEqual(object2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        object3 = rt_with_exceptions.Runner('Test1')
        object4 = rt_with_exceptions.Runner('Test2')
        for i in range(10):
            object3.run()
            object4.walk()
        self.assertNotEqual(object3.distance, object4.distance)


if __name__ == '__main__':
    unittest.main()