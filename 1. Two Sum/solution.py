class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            subs = target - nums[i]
            if subs in hashmap:
                return [hashmap[subs], i]
            hashmap[nums[i]] = i
