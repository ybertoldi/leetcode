def productExceptSelf(self, nums: List[int]) -> List[int]:
    zeroes = 0
    idx_zero = 0
    prod = 1
    for i in range(len(nums)):
        n = nums[i]
        if n == 0:
            zeroes += 1
            n = 1
            idx_zero = i
            if zeroes > 1:
                return [0] * len(nums)

        prod *= n
    
    if zeroes == 0:
        for i in range(len(nums)):
            nums[i] = prod // nums[i]
        return nums
    else:
        return [0] * (idx_zero) + [prod] + [0] * (len(nums) - idx_zero - 1)   