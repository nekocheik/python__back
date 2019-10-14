"""You are given a text, which contains different english letters and punctuation symbols.
 You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, 
"A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters."""

import re

def checkio(text: str) -> str:
    array_letters = [ 
        [],#letters
        []#Number of repetition
        ]
    text = text.lower()
    text = ''.join(sorted(text))
    text = re.sub('[^a-zA-Z]', '', text)
    for letter in text:
        if letter in array_letters[0]:
            index = array_letters[0].index(letter)
            array_letters[1][index] += 1
        else:
            array_letters[0].append(letter)
            array_letters[1].append(1)
    
    #check the letter more
    memo = 0
    index_letter = 0
    i = 0
    for number in array_letters[1]:
        if number > memo:
            memo = number
            index_letter = i
            print('ici',memo, text )
        i += 1
    
    print(array_letters[0][index_letter], index_letter)
    #replace this for solution
    return array_letters[0][index_letter]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")



#BEST SOLUTIONS

import string

def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)



from string import ascii_lowercase as letters
checkio = lambda text: max(letters, key=text.lower().count)

#https://www.programiz.com/python-programming/methods/built-in/max