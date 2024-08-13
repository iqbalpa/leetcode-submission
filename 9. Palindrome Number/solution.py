class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        m = self.reccursive(x, 0)
        print(m)
        if x == m: return True
        return False

    def reccursive(self, n, m):
        last_digit = n % 10
        remainder = n // 10
        m += last_digit
        if remainder == 0:
            return m
        m *= 10
        return self.reccursive(remainder, m)
        
