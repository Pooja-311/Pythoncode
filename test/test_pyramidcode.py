import unittest
from pyramidcode import areConsecutive

class Testpyramid(unittest.TestCase):
    def test_pyramid(self):
        self.assertEqual(areConsecutive([1,2,3],3), True)
        self.assertEqual(areConsecutive([3,4],2), False)
        self.assertEqual(areConsecutive([3],1), False)
        self.assertEqual(areConsecutive([1,1],2), False)


