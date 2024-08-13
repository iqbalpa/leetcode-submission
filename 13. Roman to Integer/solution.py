class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        temp = []
        # IX -> 1, 10
        for c in s:
            temp.append(maps[c])
        print(temp)

        result = 0
        is_larger = False
        is_more_than_3 = 0
        prev = 1_000_000
        for i in temp:
            if prev < i:
                result -= 2 * prev
                result += i
            else:
                result += i
            prev = i
        print(result)
        return result
            
        
