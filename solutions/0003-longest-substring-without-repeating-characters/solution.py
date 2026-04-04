class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        maxLength = 0
        char = set()

        while r < n:
            while s[r] in char:
                char.remove(s[l])
                l +=1
            
            char.add(s[r])
            maxLength = max(maxLength, r-l+1)
            r+=1

        return maxLength


            

             
        
