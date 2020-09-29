import re

def validateID(text):
    if re.match('^[0-9]*$', text):
        return True
    return False

def validateStr(text):
    if re.match('^[a-zA-Z]*$', text):
        return True
    return False