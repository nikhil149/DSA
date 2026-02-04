class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Track non zero index
        nonZero = 0
        # Track zero element index
        zero =0

        while zero <len(nums):
            if nonZero == zero:
                zero +=1
            elif nums[nonZero] == 0 and nums[zero] != 0:
                val = nums[nonZero]
                nums[nonZero] = nums[zero]
                nums[zero] = val 
                zero+=1
                nonZero +=1
            else:
                zero +=1
                # Move forward until zero element is found to swap
                if nums[nonZero] != 0:
                    nonZero +=1


        
