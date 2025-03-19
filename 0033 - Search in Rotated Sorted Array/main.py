def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2

        if nums[l] < nums[r]:

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1                 
        
        else:
            if target > nums[l]:
                if nums[l] > nums[m]: 
                    r = m - 1
                elif l == m:
                    r -= 1
                else:
                    if target < nums[m]:
                        r = m - 1
                    elif target > nums[m]:
                        l = m + 1
                    else:
                        return m
                    
            elif target < nums[l]: 
                if nums[l] < nums[m]: 
                    l = m + 1
                elif l == m:
                    l += 1
                else:
                    if target > nums[m]:
                        l = m + 1
                    elif target < nums[m]:
                        r = m - 1
                    else:
                        return m
            else:
                return l

    return -1