class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        def get_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
            
    # Helper 2: Simplify a fraction (numerator, denominator)
        def simplify(n: int, d: int) -> tuple[int, int]:
            # Handle negative denominators to keep the sign on the numerator
            if d < 0:
                n, d = -n, -d
            g = get_gcd(abs(n), abs(d))
            return (n // g, d // g)
    
        # DP table: Key is (numerator, denominator), Value is sequence count
        dp = {(1, 1): 1}  # Start with val = 1 (represented as 1/1)
        
        for num in nums:
            next_dp = {}
            
            for (n, d), count in dp.items():
                
                # Choice 1: Multiply (n/d * num/1 = n*num / d)
                mult_val = simplify(n * num, d)
                next_dp[mult_val] = next_dp.get(mult_val, 0) + count
                
                # Choice 2: Divide (n/d / num/1 = n / d*num)
                if num != 0:
                    div_val = simplify(n, d * num)
                    next_dp[div_val] = next_dp.get(div_val, 0) + count
                
                # Choice 3: Ignore (Leave val unchanged)
                ignore_val = (n, d)
                next_dp[ignore_val] = next_dp.get(ignore_val, 0) + count
                
            # Move to the next level of the decision tree
            dp = next_dp
            
        # Check if the exact target k (represented as k/1) is achievable
        return dp.get((k, 1), 0)
        
