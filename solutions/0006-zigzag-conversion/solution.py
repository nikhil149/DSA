class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        ans = []
        for i in range(numRows):
            for j in range(i, len(s), 2*(numRows - 1)):
                ans.append(s[j])
                diag = j+ (2* (numRows -1)) -2 * i
                if i!=0 and i != numRows -1 and diag < len(s):
                    ans.append(s[diag])

        return "".join(ans)
        
