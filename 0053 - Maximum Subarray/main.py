def maxSubArray(nums):
    maxSum = nums[0]
    curSum = 0
    
    for n in nums:
        curSum += n
        maxSum = max(curSum, maxSum)
        
        if curSum < 0:
            curSum = 0
        
    return maxSum
            
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))