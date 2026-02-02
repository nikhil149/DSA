class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = []
        remainder = 0
        my_dict = {}
        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in my_dict:
                return [my_dict[remainder], i]
            else:
                my_dict[n] = i


