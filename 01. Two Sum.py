class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                a = nums[i]+nums[j]
                if a == target:
                    return [i,j]
