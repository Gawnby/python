import unittest

# Here's our "unit".


def IsOdd(n):
    return n & 1 and True or False
IsOdd(2)
False
print ("False")
IsOdd(1)
print ("True")
True

# Here's our "unit tests".


class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))
        

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
