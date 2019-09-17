import string_calculator
import pytest

def test_empty_string():
	"""it should return 0 if the string is empty"""
	assert string_calculator.add('') == 0

def test_add_two_CSVs():
	"""it should add 2 numbers in a comma separated string"""
	assert string_calculator.add('1, 2') == 3

def test_add_multiple_CSVs():
	"""it should an unknown amount of numbers in a comma separated string"""
	assert string_calculator.add('1, 2, 3') == 6

def test_new_line_as_delimiter():
	"""it should be able to use new lines as delimiters"""
	assert string_calculator.add('1\n2,3') == 6

def test_different_delimiters():
	"""it should be able handle different delimiters"""
	assert string_calculator.add('//;\n1;2') == 3

def test_negative_numbers_exception():
	"""it should raise an exception containing all negative numbers if any are found"""
	with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2, -3\]'):
		string_calculator.add('-1, -2, -3, 1, 2, 3')

def test_bigger_than_1000():
	"""it should ignore numbers bigger than 1000"""
	assert string_calculator.add('//;\n1000,1;2') == 3

def test_delimiters_any_length():
	"""it should ignore numbers bigger than 1000"""
	assert string_calculator.add('//[***]\n1***2***3') == 6

def test_multiple_delimiters():
	"""it should be able handle multiple delimiters"""
	assert string_calculator.add('//[*][%]\n1*2%3') == 6