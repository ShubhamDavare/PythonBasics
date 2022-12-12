'''
Binary Search - For binary search, list\Array should be sorted.
                Binary search uses algorithm of divide and conquer. It divides list in two parts from middle.
                Binary search takes number of iterations as compared to linear search.


Best time complexity: O(1)
Worst time complexity: O(nlogn)
'''

a= [1, 2, 3, 7, 9, 10]


def binary_search(a, target):
    start = 0
    end = len(a) - 1

    for i in range(len(a)):

        while start <= end:
            mid = (start + end) // 2

            if a[mid] == target:
                return mid

            elif target > a[mid]:
                start = mid + 1

            else:
                end = mid - 1
        return -1


print(binary_search(a, 10))




