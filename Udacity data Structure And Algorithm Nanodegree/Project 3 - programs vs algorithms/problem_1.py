def SquareRoot(num):
    if num < 0:
        return None

    if (num == 0) or (num == 1):
        return num

    start = 0
    end = num // 2

    while start <= end:
        middle = (end + start) // 2
        middlePwr = middle * middle
        if middlePwr == num:
            return middle
        elif middlePwr < num:
            start = middle + 1
            answer = middle
        else:
            end = middle - 1

    return answer
         
  

    

print(SquareRoot(9))
print(SquareRoot(27))
print(SquareRoot(99999999))
print(SquareRoot(0))
print(SquareRoot(-98))
print(SquareRoot(630))
print(SquareRoot(1))