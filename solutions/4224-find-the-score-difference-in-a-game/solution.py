class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player1=0
        player2=0
        activePlayer = True
        for i,n in enumerate(nums):
            isOdd = n%2!=0
            if isOdd:
                activePlayer = not activePlayer
            if (i+1) %6 == 0:
                activePlayer = not activePlayer
            if activePlayer == True:
                player1 += n
            else:
                player2 += n

        return player1-player2
        
