from unittest import TestCase
from time import sleep
from threadit import Threadit, thredit_result


@thredit_result
def test_func1():
    return True


@thredit_result
def test_func2(var):
    return var


@thredit_result
def test_func3(var1, var2, var3):
    return var1 + var2 + var3


@thredit_result
def test_func4():
    sleep(3)
    return 'Hello'


def test_func5():
    return True


class TestThreditWithDecorator(TestCase):
    def test_with_no_var(self):
        run = Threadit(test_func1)
        result = run.get()
        self.assertEqual(result, True)

    def test_with_one_var(self):
        run = Threadit(test_func2, 'Hello')
        result = run.get()
        self.assertEqual(result, 'Hello')

    def test_with_more_vars(self):
        run = Threadit(test_func3, 1, 2, 3)
        result = run.get()
        self.assertEqual(result, 6)


class TestThreditWorkingStatus(TestCase):
    def test_threadit_status(self):
        run = Threadit(test_func4)
        sleep(1)

        status = run.doing_working()
        self.assertEqual(status, True)

        result = run.get()
        self.assertEqual(result, 'Hello')


class TestThreditWithoutDecorator(TestCase):
    def test_with_no_var(self):
        run = Threadit(test_func5)
        result = run.get()
        self.assertEqual(result, None)
