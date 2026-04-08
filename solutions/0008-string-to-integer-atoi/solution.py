class Solution:
    def myAtoi(self, s: str) -> int:
        updatedStr = []
        ans = 0
        isNegative = False
        isPositive = False
        for char in s:
            if (char == " " or char == '"' )and len(updatedStr) ==0 and not (isPositive == True or isNegative == True):
                continue
            elif char == "+" and not (isPositive == True or isNegative == True) and len(updatedStr) == 0:
                isPositive = True
            elif char == "-" and not (isPositive == True or isNegative == True) and len(updatedStr) == 0:
                isNegative = True
            elif char.isdigit():
                updatedStr.append(char)
                ans = ans *10 + int(char)
            else:
                break
        if len(updatedStr) == 0:
            return 0
        
        if isNegative:
            ans = ans * -1
        if ans <= (-2**31):
            return -2**31
        if ans >= (2**31 -1):
            return 2**31 -1
        return ans
        
