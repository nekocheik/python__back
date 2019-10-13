#In this mission you should check if all elements in the given list are equal.

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    memo = 'null'
    for element in elements:
        if memo == 'null':
            memo = element
        elif memo != element:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")




#BEST SOLUTIONS



def all_the_same(elements):
   return elements[1:] == elements[:-1]

'''

In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.
'''

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


if __name__ == '__main__':
    assert all_the_same([1, 1, 1])
    assert not all_the_same([1, 2, 1])
    assert all_the_same(['a', 'a', 'a'])
    assert all_the_same([])
    assert all_the_same([1])