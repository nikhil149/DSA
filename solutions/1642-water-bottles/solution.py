class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remaining = numBottles
        count = 0
        while remaining >= numExchange:
            count += remaining // numExchange
            remaining = (remaining // numExchange) + (remaining % numExchange)

        return numBottles + count


        
