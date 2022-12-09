'''
Selection Sort: 1) In selection sort we assume first element as current minimum element in the list.
                2) Using that element we traverse over the list.
                3) If we find actual minimum element in the list then we will swap that number with current minimum.
                4) After every iteration smallest element will be at the first position.

Time complexity: Worst O(n^2)
                 Best Omega(n^2)
'''

a = ['alpha', 'gamma', 'beta', 'delta']
def selection_sort(a):

    for i in range(len(a)-1):  # If n-1 elements are sorted then last element will be automatically sorted.

        min_index = i
        print(a)
        print("-"*20)
        for j in range(i+1,len(a)):  # We are taking i+1 as left side will be sorted.

            if a[min_index] > a[j]:
                min_index = j

        if min_index != i:

            a[i],a[min_index] = a[min_index],a[i]

    print(a)
    return a


selection_sort(a)
