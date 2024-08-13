class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0: return true
        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            else:
                try:
                    curr = stack.pop()
                    if curr == "(":
                        if s[i] != ")": return False
                    elif curr == "[":
                        if s[i] != "]": return False
                    elif curr == "{":
                        if s[i] != "}": return False
                except:
                    return False
        return len(stack) == 0
            
