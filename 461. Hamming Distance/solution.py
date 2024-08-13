class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # convert to binary (string)
        x = self.decToBin(x)
        y = self.decToBin(y)
        # prepend 0 in the beginning
        x, y = self.normalize(x, y)
        # count
        res = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                res += 1
        return res
        
    def decToBin(self, n: int) -> str:
        res = ''
        while n > 0:
            res = str(n % 2) + res
            n = n // 2
        return res
    
    def normalize(self, x, y) -> (str, str):
        if len(x) < len(y):
            diff = len(y) - len(x)
            x = ("0" * diff) + x
        else:
            diff = len(x) - len(y)
            y = ("0" * diff) + y
        return x, y
