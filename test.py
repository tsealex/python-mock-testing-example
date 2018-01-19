from test_obj import need_to_be_tested

from mock import patch
import unittest

# to run this test:
# python -m unittest test
@patch('test_obj.func', lambda: 50)
class TestObj(unittest.TestCase):

	def test_need_to_be_tested(self):
		self.assertEqual(need_to_be_tested(), 50)