'''
Bubble Sort: 1) After every iteration last element bubble outs to last position
             2) We compare j and j + 1 element and swap them if j + 1 element is smaller.
             3) After every iteration one element will be sorted. So we need to check len(list) - 1 iteration to skip
             already sorted elements.
Time Complexity:
 Worst time complexity is O(n^2)
 Best time complexity is O(n)

'''

a = [2,5,6,7,8,1,3]
def bubble_sort(a):

    #n = len(a) - 1

    for i in range(len(a) - 1): # Last element is already compared with condition j + 1. So we are going till len(a)-1

        print()
        print(a)
        print("-"*20)
        for j in range(len(a)-i-1): # i -1 iteration taken because it will avoid numbers which are already sorted

            if a[j+1] < a[j]:
                a[j],a[j+1] = a[j+1],a[j]
                print("\t",a)

    return a

bubble_sort(a)
