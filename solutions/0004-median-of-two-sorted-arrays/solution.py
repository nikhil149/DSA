class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArr = []
        l=0
        r=0
        N=len(nums1)
        M =len(nums2)
        while l< N and r < M:
            if nums1[l]<nums2[r]:
                newArr.append(nums1[l])
                l+=1
            else:
                newArr.append(nums2[r])
                r+=1
        
        while l< N:
            newArr.append(nums1[l])
            l+=1
        while r<M:
            newArr.append(nums2[r])
            r+=1
        val = (N+M)//2
        if (M+N) %2 !=0:
            return newArr[val]
        
        return (newArr[val]+newArr[val-1])/2


