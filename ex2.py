def isAscending(list_of_integer) :
    if len(list_of_integer) <= 1:
        return True
    if list_of_integer[0] < list_of_integer[1] :
        return isAscending(list_of_integer[1:-1])
    else :
        return False
        
print(isAscending([1,2,3,4,5,6,7]))
print(isAscending([3,4,2,5,6,1,2]))
print(isAscending([9,8,7,6,5,4]))
print(isAscending([0,0,1,1,2,2,3,3,4,4,5,5]))
print(isAscending([6,7,8,9,10,11,12]))
print(isAscending([6,3,8,7,9,2,3,1,5]))