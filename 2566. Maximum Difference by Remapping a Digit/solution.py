class Solution:
    def minMaxDifference(self, num: int) -> int:
        n = str(num)
        i = 0
        first = '9'
        while first == '9' and i < len(n):
            first = n[i]
            i += 1
        max_val = n.replace(first, '9')
        max_val = int(max_val)

        m = str(num)
        first = m[0]
        min_val = m.replace(first, '0')
        min_val = int(min_val)

        print(max_val, min_val)
        return max_val - min_val