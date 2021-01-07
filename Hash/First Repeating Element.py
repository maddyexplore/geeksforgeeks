def firstRepeated(arr, n):
    
    #arr : given array
    #n : size of the array
    for i in range(n):
        if arr.count(arr[i])>1:
            return(i+1)
    else:
        return(-1)
