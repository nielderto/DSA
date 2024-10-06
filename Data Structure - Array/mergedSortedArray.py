def merge_sorted_array(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2
    
    merged_array = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
            
        else:
            merged_array.append(arr2[j])
            j += 1
                
    return merged_array + arr1[i:] + arr2[j:]


print(merge_sorted_array([0,3,4,31], [4,6,30]))