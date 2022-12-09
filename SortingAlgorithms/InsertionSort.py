'''
Insertion Sort: Here we divide list in two parts sorted and un sorted.
                2) We assume first elements as sorted. Then we compare that element with next element in un sorted list.
                3) If next element is smaller than element in sorted list we insert smallest element in sorted part
                   at correct position.


Worst time complexity: O(n^2)
Best time Complexity:  O(n)

'''

a = [2, 8, 7, 3, 5, 1]

def insertion_sort_annotated(a):
    # We are starting at position 1 because initially we considered element at zeroth # position as sorted
    for i in range(1, len(a)):


        print(a[:i],"|",a[i:]) # Displays how boundry changes after every iteration.
        print("-"*20)
        index_tobe_inserted = i
        j = i - 1  # For comparing previous element with element at ith position

        while j >= 0:

            if a[j] < a[index_tobe_inserted]:
                break

            a[j],a[index_tobe_inserted] = a[index_tobe_inserted],a[j]
            index_tobe_inserted = j
            j -= 1


    return a

print(insertion_sort_annotated(a))