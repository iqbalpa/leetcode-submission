class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2 == []:
            return nums1
        a, b, write_idx = m-1, n-1, m+n-1
        while write_idx >= 0:
            if a >= 0 and b >= 0 and nums1[a] > nums2[b]:
                nums1[write_idx] = nums1[a]
                nums1[a] = 0
                write_idx -= 1
                a -= 1
            elif a >= 0 and b >= 0 and nums1[a] <= nums2[b]:
                nums1[write_idx] = nums2[b]
                nums2[b] = 0
                write_idx -= 1
                b -= 1
            elif a < 0 and b >= 0:
                nums1[write_idx] = nums2[b]
                write_idx -= 1
                b -= 1
            else:
                nums1[write_idx] = nums1[a]
                write_idx -= 1
                a -= 1
                
