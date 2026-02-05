class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=nums[:]
        # For result index
        r =0 
        # for current nums index
        n=0
        for i, n in enumerate(nums):
            if n > 0:
                new_index = (n+i)%len(nums)
                result[i] = nums[new_index]
            elif n< 0:
                if (n+i)<= 0:
                    new_index = -1 * (abs(n+i)%len(nums))
                    result[i] = nums[new_index]
                else:
                    new_index =  (abs(n+i)%len(nums))
                    result[i] = nums[new_index]
            else:
                result[i] = nums[i]
        return result
        
