def maxSubArray(nums):
    res = nums[0]
    curMin, curMax = 1, 1
    
    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        
        temp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(temp, n * curMin, n)    
        res = max(res, curMax, curMin)
    
    return res
            
print(maxSubArray([2,3,-2,4]))
print(maxSubArray([-2,0,-1]))