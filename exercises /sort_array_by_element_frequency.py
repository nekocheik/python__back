"""Sort the given iterable so that its elements end up in the decreasing frequency order, 
that is, the number of times they appear in elements. If two elements have the same frequency, 
they should end up in the same order as the first appearance in the iterable."""


from collections import Counter

def frequency_sort(items):
    # your code here
    c = sorted(items)
    counter = Counter(items).most_common(3);
    items = []
    for count in counter:
        for i in range(0,count[1]):
            items.append(count[0])
    
    print(items)
    return items


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

#BEST SOLUTIONS

def frequency_sort(items):
    return sorted(items, key = lambda x: (-items.count(x), items.index(x)))