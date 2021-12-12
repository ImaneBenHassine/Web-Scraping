# -*- coding: utf-8 -*-
"""
   - $2.6 million--> 2600000 # the word syntax

   - $858,000 --> 858000 # the value syntax

   - $4,000,000 (estimated)

   - 60 million Norwegian Kroner (around $8.7 million in 1989)

   - ['131\xa0crore']

   - $75–90 million
"""
import re

# r for write text ,\ to find digit, d for digits
# allows to grab numbers \.*\d to add in the pattern other digits, ,\d{3} follows by group of 3 digit

amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"
# ? to check if exist or not , | for or
standard = fr"\${number}(-|\sto\s)?({number})?\s({amounts})"

def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict.get(word.lower(), 1)

def parse_word_syntax(string):
    stripped_string = string.replace(",", "")
    value = float(re.search(number, stripped_string).group())
    modifier = word_to_value(re.search(amounts, string, flags=re.I).group()) # flags to ignore the case of million or billion
    return value*modifier

def parse_value_syntax(string):
    stripped_string = string.replace(",", "")
    return float(re.search(number, stripped_string).group())

def money_conversion(money):
    if type(money) == list:
        money = money[0]

    word_syntax = re.search(standard, money, flags=re.I)
    value_syntax = re.search(fr"\${number}", money)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())
    elif value_syntax:
        return parse_value_syntax(value_syntax.group())
    else:
        return None
print