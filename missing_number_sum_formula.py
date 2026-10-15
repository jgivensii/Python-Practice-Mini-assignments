"""
    This is a coding problem where an unsorted list is given 
    containing the sequential integers from 1 to N, except one number 
    is missing. 
    
    [TASK]
        Write a Python function that uses the sum formula to find the missing number.
"""

#=====================
# APPROACH
#=====================

"""
    Utilize Gauss's sum equation:
        
        f(n_min, n_max) = (n_max - n_min + 1 )(n_max+n_min)/2
        
    where n_max is where the max number N in the list and n_min is where the list is
    beginning at, in this case 1. 
    
    The list will have N-1 elements. Thus summing the elements in the list and then finding
    difference from f(n) should give the missing number.
"""

#=======================
# PSEUDOCODE DESCRIPTION
#=======================

"""
    nums: list[int] = [some N-1 list of unsorted of numbers between 1 to N]
    
    n_max: int = maximum(num)
    n_min: int = minimum(num)
    
    Gauss's sum function:
        f(n_min,n_max) = (n_max - n_min + 1 )(n_max+n_min)/2
        return f(n_min, n_max)
    
    Difference function:
       missing_number = f(n_min,n_max) - sum(list)
       
       return missing_number
       
    print(missing_number)
"""

#==================
# CODE SOLUTION
#==================


nums: list[int] = [3, 1, 4, 5] # expected output: 2



def gauss_sum(num: list[int]) -> int:
    n_max: int = max(num)
    n_min: int = min(num)
    return ((n_max - n_min + 1)*(n_min + n_max))/2

def difference(num: list[int]) -> int:
    return gauss_sum(num) - sum(num)


if __name__ == "__main__":
    print(difference(nums))
    
#    This does indeed output 2, and should out put any missing number 
#    from any sequential list from n_min to n_max, as seen with the next
#    example from 20 to 26 where 23 is missing.

    example: list[int] = [20,21,22, 24, 25]
    print(difference(example))
