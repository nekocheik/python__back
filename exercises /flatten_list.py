"""Nicola likes to categorize all sorts of things.
 He categorized a series of numbers and as the result of his efforts, a simple sequence of numbers became a deeply-nested list. 
 Sophia and Stephan don't really understand his organization and need to figure out what it all means. 
 They need your help to understand Nikolas crazy list.
There is a list which contains integers or other nested lists which may contain yet more lists and integers which then… you get the idea. 
You should put all of the integer values into one flat list. 
The order should be as it was in the original list with string representation from left to right."""



def recursive(array: list):
    new_array = []
    for value in array:
        if type(value) == list:
            new_value = recursive(value)
            for value2 in new_value:
                new_array.append(value2)
        else:
            new_array.append(value)
    return new_array

def flat_list(array):
    return recursive(array)

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')



#best solutions

flat_list =f=lambda d:[d]if int==type(d)else sum(map(f,d),[])


def flat_list(l):
    r = []
    def f(l):
        for i in l:
            r.append(i) if type(i) is int else f(i)
    f(l)
    return r

def flat_list(array):
    try:
        return [int(array)]
    except:
        return sum(map(flat_list, array), [])


flat_list=lambda a:eval('['+str(a).replace('[','').replace(']','')+']')#73