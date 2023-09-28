class Solution(object):
    def singleNumber(self, nums):
        obj = []
        for i in range(len(nums)):
            if nums[i] in obj:
                obj.remove(nums[i])
            else:
                obj.append(nums[i])
        return max(obj)



# Example 1:
# Input: nums = [2,2,1]
# Output: 1
