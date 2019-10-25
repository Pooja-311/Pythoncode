import unittest
from example4 import reverse_st


class Testreverse(unittest.TestCase):
    def test_reverse(self):

        self.assertEqual(reverse_st("this$ istherevers e#"),'esre$ verehtsisih t#')
        self.assertEqual(reverse_st("!ooja%here@"),'!ereh%ajoo@')
        self.assertEqual(reverse_st("!yyain*patil%"),'!litap*niayy%')

