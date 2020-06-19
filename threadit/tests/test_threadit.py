from unittest import TestCase
from time import sleep
from threadit import Threadit


def test_func1():
    return True


def test_func2(var):
    return var


def test_func3(var1, var2, var3):
    return var1 + var2 + var3


def test_func4():
    sleep(3)
    return 'Hello'


def test_func5(var1, var2, var3, num1=0, num2=0):
    return var1 + var2 + var3 + num1 + num2


def test_func6():
    sleep(10)
    return 'Hello'


class TestThredit(TestCase):
    def test_with_no_var(self):
        run = Threadit(test_func1)
        result = run.result()
        self.assertEqual(result, True)

    def test_with_one_var(self):
        run = Threadit(test_func2, 'Hello')
        result = run.result()
        self.assertEqual(result, 'Hello')

    def test_with_more_vars(self):
        run = Threadit(test_func3, 1, 2, 3)
        result = run.result()
        self.assertEqual(result, 6),

    def test_with_vars_and_kwargs(self):
        run = Threadit(test_func5, 1, 2, 3, num1=5, num2=5)
        result = run.result()
        self.assertEqual(result, 16)


class TestThreditWorkingStatus(TestCase):
    def test_threadit_status(self):
        run = Threadit(test_func4)
        sleep(1)

        status = run.doing_work()
        self.assertEqual(status, True)

        result = run.result()
        self.assertEqual(result, 'Hello')


class TestThreditTimeout(TestCase):
    def test_threadit_status(self):
        run = Threadit(test_func4)
        sleep(1)

        status = run.doing_work()
        self.assertEqual(status, True)

        result = run.result(timeout=1)

        self.assertEqual(result, None)


