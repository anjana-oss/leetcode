class Solution(object):
    def twoSum(self, nums, target):
        mp={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in mp:
                return [min(mp[diff],i),
                max(mp[diff],i)]
            mp[n]=i
        