# -*- coding: utf-8 -*-


import pytest
from conversion import money_conversion

def test_standard():
	assert money_conversion("$5 million") == 5000000

def test_standard_double_digit():
	assert money_conversion("$88 million") == 88000000

def test_standard_with_decimal():
	assert money_conversion("$5.8 million") == 5800000

def test_standard_multiple_decimals():
	assert money_conversion("$4.258 million") == 4258000

def test_standard_billion():
	assert money_conversion("$2.15 billion") == 2150000000

def test_standard_thousand():
	assert money_conversion("$990.9 thousand") == 990900

def test_range():
	assert money_conversion("$8.6-7 million") == 8600000

def test_range_with_to():
	assert money_conversion("$8.7 to 9 million") == 8700000

def test_number():
	assert money_conversion("$870000") == 870000

def test_number_with_commas():
	assert money_conversion("$879,589,000") == 879589000

def test_number_with_commas_and_decimals():
	assert money_conversion("$25,000,000.80") == 25000000.8

def test_number_with_commas_middle():
	assert money_conversion("estimated $47,000,000 (USD)") == 47000000

def test_other_currency():
	assert money_conversion("60 million Norwegian Kroner (around $8.7 million in 1989)") == 8700000

def test_list():
	assert money_conversion(['$523.6 million (gross)', '$378.5 million (net)']) == 523600000

def test_unkown():
	assert money_conversion("80 crore") is None
