def twoSum(self, nums: list[int], target: int) -> list[int]:
    table = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in table:
            return [i, table[num]]
            
        table[target - num] = i
