def Min_Max(ints):


    min ,max = None,None

    for index, value in enumerate(ints):

        if index == 0:
            min = value
            max = value

        if value < min:
            min = value
        elif value > max:
            max = value

    return min, max



import random


Case1 = [i for i in range(0, 10)]  # a array containing 0 - 9

random.shuffle(Case1)


print ("Pass" if ((0, 9) == Min_Max(Case1)) else "Fail")  #pass




print ("Pass" if ((None, None) == Min_Max([])) else "Fail") #pass



print ("Pass" if ((1, 1) == Min_Max([1])) else "Fail") #pass
