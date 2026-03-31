class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l=0
        r=len(height) -1
        while l<r:
            minHeight = min(height[l], height[r])
            diff = r-l
            if height[l] < height[r]:
                l+=1
            else: 
                r-=1        
            area = minHeight * diff
            if area > maxArea:
                maxArea = area
        return maxArea




        
