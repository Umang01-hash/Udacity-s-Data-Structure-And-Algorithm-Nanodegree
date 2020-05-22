def rotated_array_search(arr, num):

    return RecursiveArraysearch(arr,num,0,len(arr) - 1)


def RecursiveArraysearch(arr, num, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2
    midEle = arr[mid]

    if midEle == num:
        return mid

    if arr[start] <= midEle:

        if midEle > num and arr[start] <= num:
            return RecursiveArraysearch(arr, num, start, mid - 1)
        return RecursiveArraysearch(arr, num, mid + 1, end)

    if midEle < num and arr[end] >= num:
        return RecursiveArraysearch(arr, num, mid + 1, end)
    return RecursiveArraysearch(arr, num, start, mid - 1)


def LinearSearch(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# Tests

def test_function(test_case):
    arr = test_case[0]
    number = test_case[1]
    if LinearSearch(arr, number) == rotated_array_search(arr,
                                                                 number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[],10])  #Empty List
test_function([[7],7])  #Single Input list
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3])  #non-rotated array
test_function([[9,8,7,6,5,1,4,3,2],5])



