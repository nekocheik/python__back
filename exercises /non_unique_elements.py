"""You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
"""

#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:
    memo = [
        data[:],
        data[:]
        ]
    count = 0
    i = 0
    for num in memo[0]:
        for memo_num in memo[1]:
            if memo_num == num:
                count += 1
        if count == 1:
            print('delet', data[i], i)
            del data[i]
        else:
            i += 1
        count = 0
    
    print(data)
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #replace this for solution
    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")


#BEST SOLUTIONS


from collections import Counter


def checkio(data):
    counter = Counter(data)
    return [item for item in data if counter[item] > 1]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"