"""
    This is an education review of the different sorting methods and runtime complexity analysis. Given the O(n^2) of the bubble sort method. 
    It is highly not recommended to use in production apps due to the lack of scalability. But understanding of 
    the fundemental sorting methods is beneficial for more optimized sorting methods. 
"""


def bubble_sort(arr: list[int]) -> tuple[list[int], int]:
    n = len(arr) # 1 operation
    swap_count = 0 # 

    for i in range(n): # n operations
        swapped = False # 1 operation

        for j in range(0, n - i - 1): # n operations # This type of nested loop produces a runtime complexity of n(n-1)/2
            if arr[j] > arr[j + 1]: # 1 operation
                # TODO: swap arr[j] and arr[j+1]
                arr_swap = arr[j+1] # 1 operation 
                arr[j+1] = arr[j] # 1 operation
                arr[j] = arr_swap # 1 operation
                # TODO: increment swap_count
                swap_count = swap_count + 1 # 1 operation
                # TODO: mark swapped = True
                swapped = True # 1 operation
                pass
        
        # TODO: if no swaps happened, break early
        if swapped == False: # 1 operation
            break
    return arr, swap_count 

"""
    Full runtime complexity for this model would be 
    
    Outer loop: 2 primitive operations n times -> 2n
    
    Inner loop: 6 primitive operations n(n-1)/2 times -> 3n^2 - 3n
    
    General: 3 primitive operations (2 equivalence and 1 return) -> 3
    
    Full model: f(n) = 3n^2-n+3 
    
    Big O notation: O(n^2)
"""


if __name__ == "__main__":
    print(bubble_sort([5,1,4,2,8]))