def findMin(nums):
    l = 0
    r = len(nums) - 1
    while r > l:
        
        m = (r + l) // 2

        if nums[r] < nums[m]:
            l = m + 1
        else:
            r = m
        
    
    return nums[l]