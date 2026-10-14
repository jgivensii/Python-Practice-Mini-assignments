"""
    This is an education review of the different sorting methods and runtime complexity analysis. 
"""

def merge_sort(arr: list[int]) -> tuple[list[int], int]:
    result = []
    count = 0
    i = 0
    j = 0
    if len(arr) <= 1:
        return arr, 0
    right, right_merges = merge_sort(arr[int(.5*len(arr)):])
    left, left_merges = merge_sort(arr[:int(.5*len(arr))])
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
            
        else:
            result.append(right[j])
            j = j + 1 
            
    while i < len(left):
            result.append(left[i])
            
            i = i + 1 
    while j < len(right):
            result.append(right[j])
            j = j + 1 
        
        
     
    count = 1 + count 
    
    total = count + right_merges + left_merges     
    return result, total
            
if __name__ == "__name__":
    print(merge_sort([38,27,43,3,9,82,10]))