class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start =0
        for i, n in enumerate(nums):
            if n == target:
                return i
            else:
                if target > n:
                    start += 1
                else:
                    return start
        
        return start
