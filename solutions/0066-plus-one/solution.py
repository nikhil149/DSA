class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = int(''.join(str(x) for x in digits))
        value += 1
        
        result = list(map(int,str(value)))
        return result
        
