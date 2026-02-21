#17-08-2025 | 09-02-2026 
def find_target(arr, target):
    i=0
    j=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                n = arr[i]+arr[j]
                if n == target:
                    return [i,j]
             
    return 'Target not found'
