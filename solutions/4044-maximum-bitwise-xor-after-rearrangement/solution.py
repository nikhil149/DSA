class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        # Count the available 0s and 1s in string t
        zeros_in_t = t.count('0')
        ones_in_t = t.count('1')
        
        result = []
        
        # Iterate through s from left to right to maximize the most significant bits
        for char in s:
            if char == '1':
                # We want a '0' to make XOR result '1'
                if zeros_in_t > 0:
                    result.append('1')
                    zeros_in_t -= 1
                else:
                    # Forced to use a '1', making XOR result '0'
                    result.append('0')
                    ones_in_t -= 1
            else: # char == '0'
                # We want a '1' to make XOR result '1'
                if ones_in_t > 0:
                    result.append('1')
                    ones_in_t -= 1
                else:
                    # Forced to use a '0', making XOR result '0'
                    result.append('0')
                    zeros_in_t -= 1
                    
        return "".join(result)
        
