"""Stephan and Sophia forget about security and use simple passwords for everything.
 Help Nikola develop a password security check module. 
 The password will be considered strong enough if its length is greater than or equal to 10 symbols,
  it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
  The password contains only ASCII latin letters or digits."""

import re

def checkio(password: str) -> bool:
    if re.match("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)([\w]{10,})$", password):
       memo = True
    else:
       memo = False
    #replace this for solution
    return memo

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


#BEST SOLUTIONS

import re

DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')

def checkio(data):
    """
    Return True if password strong and False if not
    
    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False
    
    if not DIGIT_RE.search(data):
        return False

    if not UPPER_CASE_RE.search(data):
        return False

    if not LOWER_CASE_RE.search(data):
        return False
        
    return True
