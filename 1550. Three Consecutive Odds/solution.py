class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = 3
        count_consec_true = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                count_consec_true += 1
            else: 
                count_consec_true = 0
            if count_consec_true == 3:
                return True
        return False
        