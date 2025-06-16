# Write your code here
import re

def only_letters(string):
    return re.fullmatch(r'[a-zA-Z]*', string) is not None