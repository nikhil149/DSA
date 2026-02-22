class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        def getFactorial(num):
            return 1 if num <= 1 else num * getFactorial(num-1)

        total =0
        actual_num = n
        while n >0:
            num = n%10
            total += getFactorial(num)
            n = n//10
        return sorted(str(actual_num))==sorted(str(total))
            
        
