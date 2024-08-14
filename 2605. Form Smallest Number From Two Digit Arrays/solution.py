class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        hashmap = {}
        # e1e2
        for e1 in nums1:
            hashmap[e1] = 100
            for e2 in nums2:
                if e1 == e2:
                    hashmap[e1] = e1
                    break
                temp = e1 * 10 + e2
                if temp < hashmap[e1]:
                    hashmap[e1] = temp
        # e2e1
        for e2 in nums2:
            hashmap[e2] = 100
            for e1 in nums1:
                if e1 == e2:
                    hashmap[e2] = e2
                    break
                temp = e2 * 10 + e1
                if temp < hashmap[e2]:
                    hashmap[e2] = temp

        res = 100
        for k in hashmap:
            if hashmap[k] < res:
                res = hashmap[k]
        return res
