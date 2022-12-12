'''
Linear Search - Linear search is used for unsorted list\array.
                Enumrate function return a list of tuple containing of index and value pair.

Worst time complexity : O(n)
Best time complexity: O(1) That element is found at first index
'''

a = [2,5,7,8,1,4]

def linear_search(a,target):
    for key,value in enumerate(a):

        if value == target:
            return key
    return -1

print(linear_search(a,4))
