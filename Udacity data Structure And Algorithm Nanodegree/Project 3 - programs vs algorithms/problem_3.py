def rearrange_digits(arr):


    mid = len(arr) // 2


    L1 = arr[:mid]
    L2 = arr[mid:]
    L1 = mergeSort(L1)
    L2 = mergeSort(L2)

    result = [int("".join([str(item) for item in L1]))]
    result.append(int("".join([str(item) for item in L2])))
    return result



def mergeSort(input_list):

    input_list = merge_sort_recur(input_list)  #HELPER FUNCTION FOR MERGE SORT
    return input_list


def merge_sort_recur(input_list):

    size = len(input_list)
    if (size == 1):
        return input_list

    mid = len(input_list) // 2
    left = input_list[0:mid]
    right = input_list[mid:]

    return merge(merge_sort_recur(right), merge_sort_recur(left), False)


def merge(left, right, ascending = True):
    result = []
    Lindex = 0
    Rindex = 0

    while Lindex < len(left) and Rindex < len(right):
        if ascending:
            # ascending sort
            if left[Lindex] < right[Rindex]:
                result.append(left[Lindex])
                Lindex += 1
            else:
                result.append(right[Rindex])
                Rindex += 1
        # descending sort
        else:
            if left[Lindex] > right[Rindex]:
                result.append(left[Lindex])
                Lindex += 1
            else:
                result.append(right[Rindex])
                Rindex += 1

    # add any remaining items from the left array
    while Lindex < len(left):
        result.append(left[Lindex])
        Lindex += 1


    while Rindex < len(right):
        result.append(right[Rindex])
        Rindex += 1


    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [21, 543]])
test_case = [[4, 6, 2, 5, 9, 8], [642, 985]]
test_function(test_case)

print(rearrange_digits([1, 2, 3, 4, 5]))
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
print(rearrange_digits([0, 2, 4, 6, 8]))
print(rearrange_digits([11, 9, 3, 9]))
