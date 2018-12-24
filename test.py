import unittest

class Test:
    def gen4567(self):
        yield 4
        yield 5
        yield 6
        yield 7

    def change(self,x):
        x[0] = x[0]+5

class Testcase(unittest.TestCase):
    def setUp(self):
        self.t = Test()

    def test_test(self):
        def fun(a):
            if a == 0:
                raise Exception(ZeroDivisionError, 'jhaha')
            else:
                return 1/a
        i = iter(self.t.gen4567())
        self.assertEqual(next(i), 4)
        self.assertEqual(i.__next__(), 5)
        self.assertEqual(next(i), 6)
        self.assertEqual(next(i), 7)
        self.assertRaises(ZeroDivisionError, fun(0))
        # self.assertRaises(StopIteration, i.__next__())

if __name__ == '__main__':
    unittest.main()
    # t = Test()
    # g = lambda: t.gen4567().__next__()
    # print(g)
    # print(type(ZeroDivisionError))
    
    

    