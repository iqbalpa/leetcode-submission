class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        k = 0
        prev = -999
        for i in range(len(nums)):
            if nums[i] == prev:
                print(i)
                prev = nums[i]
                pass
            else:
                print("k", i)
                nums[k] = nums[i]
                prev = nums[i]
                k += 1
        return k
