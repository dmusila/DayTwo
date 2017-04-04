def data_type(datainput):


	if datainput is None:
		return "no value"

	elif type(datainput) is str:
		return len(datainput)
	elif type(datainput) is bool:
		return datainput
	elif type(datainput) is int:
		if datainput == 100:
			return "equal to 100"
		elif datainput < 100:
			return "less than 100"
		else:
			return "more than 100"
	elif type(datainput) is list:
		if len(datainput)< 3:
			return None
		else:
			return datainput[2]
		
#TEST >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import unittest

class CarClassTest(unittest.TestCase):


  def test_none_type(self):
    self.assertEqual('no value', data_type(None))

  def test_array_type(self):
    self.assertEqual(3, data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', data_type(200))

  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))

unittest.main()
