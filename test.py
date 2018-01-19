import test_obj

from unittest.mock import MagicMock
import unittest

# to run this test:
# python -m unittest test
# @patch('test_obj.func', lambda: 50)
class TestObj(unittest.TestCase):

	def test_need_to_be_tested(self):
		test_obj.func = MagicMock(return_value=50)
		#mock = unittest.mock.create_autospec(need_to_be_tested)
		#mock.func.return_value = 50
		self.assertEqual(test_obj.need_to_be_tested(), 50)
