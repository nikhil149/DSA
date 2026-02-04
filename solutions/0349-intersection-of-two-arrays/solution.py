class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using built in set functions
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set1.intersection(set2))

        left = 0
        right =0
        # Sorting both arrays
        nums1.sort()
        nums2.sort()
        intersection_list = set()

        while left< len(nums1) and right<len(nums2):
            if nums1[left] == nums2[right]:
                intersection_list.add(nums1[left])
                left += 1
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1 
            else:
                right += 1

        return list(intersection_list)
                

