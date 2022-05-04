##################################################
##  Problem 1. common
##################################################

# Given an array of lists of distinct numbers, 
# return the number of numbers common to all lists

def common(lists):
    '''
    Input:  lists  | Array of arrays of positive integers
    Output: num_common  | number of numbers common to all arrays
    '''
    
    num_common = 0
    
    if([] in lists) or len(lists) == 0:
        return 0
    
    if(len(lists) == 1):
        return len(lists[0])

    for i in range(len(lists)):
        if i == 0:
            common = lists[i]
        else:
            common = set(common) & set(lists[i])

    num_common = len(common)
            
    return num_common
