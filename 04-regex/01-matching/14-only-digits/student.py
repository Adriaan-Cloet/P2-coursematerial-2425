# Write your code here
import re

def only_digits(string):
    return re.fullmatch(r'\d*', string) is not None