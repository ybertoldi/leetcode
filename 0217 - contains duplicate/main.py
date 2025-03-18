def containsDuplicate(nums):
    numSet = {}
    
    for num in nums:
        if num in numSet:
            return True
        numSet.add(num)
    
    return False
    
print(containsDuplicate([1,2,3,1]))
